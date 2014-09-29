# coding=utf-8
import htmlentitydefs
from django.utils.translation import ugettext_lazy as _
import re
from cms.models import CMSPlugin
from . import geocode
from django.db import models
from django.utils.html import strip_tags
from django.conf import settings
import logging
import HTMLParser
logger = logging.getLogger(__name__)



class AgendaModel(CMSPlugin):
    nb_last_event = models.IntegerField(u'nombre d\'event', default=3)


class EntryZiniaCmsPlugins(CMSPlugin):
    nb_last_post = models.IntegerField(u"nombre de post", default=3)


class Professeur(models.Model):
    nom = models.CharField(u'Nom', max_length=50)
    prenom = models.CharField(u'Prénom', max_length=50)
    date_naissance = models.DateField(u"Date de naissance", null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, editable=False)
    date_update = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    email = models.EmailField(blank=True, null=True)
    tel = models.CharField(blank=True, null=True, max_length=15)

    def __unicode__(self):
        return u"%s %s" % (self.nom, self.prenom)

    class Meta:
        verbose_name = u"Professeur"
        verbose_name_plural = u"Professeurs"

class Eleve(models.Model):
    nom = models.CharField(u'Nom', max_length=50)
    prenom = models.CharField(u'Prenom', max_length=50)

class PaysModel(models.Model):
    label = models.CharField(u"nom pays", max_length=50)

    def __unicode__(self):
        return self.label


class RegroupementSalle(models.Model):
    nom = models.CharField(max_length=60, null=True)
    pays = models.ForeignKey(PaysModel, null=True)

    def __unicode__(self):
        return u"{} {}".format(self.nom, self.pays)

class ListeProfesseur(CMSPlugin):
    pass

class ListeSalle(CMSPlugin):
    pays = models.ForeignKey(PaysModel)

class Salle(models.Model):
    nom = models.CharField(u'Nom', max_length=50)
    professeurs = models.ManyToManyField(Professeur, null=True, blank=True)
    horaire = models.TextField(u"Horaire", null=True, blank=True)
    adresse = models.CharField(u"adresse", max_length=500, null=True)
    description = models.TextField(u'description', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, editable=False)
    date_update = models.DateTimeField(auto_now=True, auto_now_add=True, editable=False)
    ville = models.CharField(u"nom ville", null=True, max_length=200)
    pays = models.ForeignKey(PaysModel)
    secteur = models.ForeignKey(RegroupementSalle, null=True, blank=True)

    computed_address = models.CharField(_('Computed address'), max_length=255, null=True, blank=True)
    latitude = models.FloatField(_('Latitude'), null=True, blank=True)
    longitude = models.FloatField(_('Longitude'), null=True, blank=True)
    geocode_error = models.BooleanField(_('Geocode error'), default=False)

    @property
    def adresse_plain(self):
        a = re.sub(r'\r\n|\r|\n|&nbsp|;', ' ', strip_tags(self.adresse))
        html_parser = HTMLParser.HTMLParser()
        unescaped = html_parser.unescape(a)
        a = decodeHtmlText(unescaped)
        return a

    def __unicode__(self):
        return self.nom

    def marker(self):
        url = '/salles/salle/{}/#{}'
        if self.secteur:
            url = url.format(self.secteur.pk, self.pk)
        else:
            return None
        return u'[\"{}\", {}, {}, \'{}\']'.format(self.nom, self.latitude, self.longitude, url)

    def fill_geocode_data(self):
        if not self.adresse_plain:
            self.geocode_error = True
            return
        try:
            do_geocode = getattr(settings, "EASY_MAPS_GEOCODE", geocode.google_v3)
            result = do_geocode(self.adresse_plain)
            if result:
                self.computed_address, (self.latitude, self.longitude,) = result
                self.geocode_error = False
            else:
                self.geocode_error = True
        except geocode.Error as e:
            try:
                logger.error(e)
            except Exception:
                logger.error("Geocoding error for address %s", self.adresse_plain)

            self.geocode_error = True
            # TODO: store the exception


def decodeHtmlText(html):
    """
    Given a string of HTML that would parse to a single text node,
    return the text value of that node.
    """
    # Fast path for common case.
    if html.find("&") < 0: return html
    return re.sub(
        '&(?:#(?:x([0-9A-Fa-f]+)|([0-9]+))|([a-zA-Z0-9]+));',
        _decode_html_entity,
        html)

def _decode_html_entity(match):
    """
    Regex replacer that expects hex digits in group 1, or
    decimal digits in group 2, or a named entity in group 3.
    """
    hex_digits = match.group(1)  # '&#10;' -> unichr(10)
    if hex_digits: return unichr(int(hex_digits, 16))
    decimal_digits = match.group(2)  # '&#x10;' -> unichr(0x10)
    if decimal_digits: return unichr(int(decimal_digits, 10))
    name = match.group(3)  # name is 'lt' when '&lt;' was matched.
    if name:
        decoding = (htmlentitydefs.name2codepoint.get(name)
            # Treat &GT; like &gt;.
            # This is wrong for &Gt; and &Lt; which HTML5 adopted from MathML.
            # If htmlentitydefs included mappings for those entities,
            # then this code will magically work.
            or htmlentitydefs.name2codepoint.get(name.lower()))
        if decoding is not None: return unichr(decoding)
    return match.group(0)
