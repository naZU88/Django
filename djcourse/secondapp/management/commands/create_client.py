from django.core.management.base import BaseCommand
from secondapp.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com',
        phone_number='+7987654321', adress='Some fake adress')
        client.save()
        self.stdout.write(f'{client}')
