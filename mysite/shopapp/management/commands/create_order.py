from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create orger")
        user = User.objects.get(username="admin")
        order = Order.objects.get_or_create(
            delivery_address="Adf, d 1",
            promocode="Sale123",
            user=user,
        )
        self.stdout.write(f"Create orger {order}")
