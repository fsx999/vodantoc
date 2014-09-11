from django.core.management.base import BaseCommand
from base.models import Salle
class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        for salle in Salle.objects.all():
            salle.save()
