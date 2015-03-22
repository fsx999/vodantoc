# coding=utf-8
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from base.models import Eleve

class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        obj = "Annulation du cours de Vo Dan Toc du mardi 24 mars 2015"
        text = u"""
Cher(e)s adhérent(e)s

Nous vous informons que le cours de Vo Dan Toc du mardi 24 mars 2015 qui a lieu au gymnase La Source est annulé car la salle a été réquisitionnée pour l'équipe féminine de handball.
Les cours reprennent donc le vendredi 27 mars 2015 à 18h pour les enfants et 19h pour les adultes.

A bientôt.
Martialement vôtre.
L'école française de Vo Dan Toc

         """
        for x in Eleve.objects.filter(inscription__salle__pk=1, inscription__annee__annee=2014, email__isnull=False, inscription__principale=True):
            send_mail(obj, text, 'ef.vodantoc@gmail.com', [x.email])