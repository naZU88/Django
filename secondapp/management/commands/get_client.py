from django.core.management.base import BaseCommand
from secondapp.models import Client


class Command(BaseCommand):
    help = "Get client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client}')
