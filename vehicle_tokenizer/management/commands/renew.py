from django.core.management.base import BaseCommand
from vehicle_tokenizer.models import Vehicle

class Command(BaseCommand):
    help = 'renew the fuel quota'

    def handle(self,*args,**kwargs):
        vehicles = Vehicle.objects.all()
        print("renewing the fuel quota of all vehicles please wait...")
        for vehicle in vehicles:
            vehicle.usage = 0
            vehicle.save()
        print("renewel finished!")
