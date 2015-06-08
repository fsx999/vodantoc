# coding=utf-8
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from base.models import Eleve

class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        obj = "Annulation du cours de Vo Dan Toc du mardi 24 mars 2015"
        text = u"""
Chers Vo-shins,

C'est avec plaisir que nous vous convions à la fête de fin d'année de l'EFVDT.
Elle se déroulera ce samedi 13 juin à partir de 18h00, au théâtre de l'Espace Icare 31 boulevard Gambetta 92130 Issy Les Moulineaux.

A cette occasion, emmenez famille et amis afin de leur faire découvrir le Vo Dan Toc grâce au spectacle de fin d'année.

Assistez à la remise des diplômes des enfants.

Un apéritif dinatoire clôturera la soirée pour lequelle chacun prévoira boissons et gourmandises.

Venez nombreux.


L'EFVDT


         """
        for x in Eleve.objects.filter(inscription__salle__pk=1, inscription__annee__annee=2014, email__isnull=False, inscription__principale=True):
            try:
                send_mail(obj, text, 'ef.vodantoc@gmail.com', [x.email])
            except:
                pass