from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    """
        Creates products
    """

    def handle(self, *args, **options):
        self.stdout.write("creates products")
        products_names = [
            'Laptop',
            'Desktop',
            'Smartphone',
        ]
        for products_name in products_names:
            product, create = Product.objects.get_or_create(name=products_name)
            if create:
                self.stdout.write(f"Create product {products_name}")
            else:
                self.stdout.write(f"{products_name} is already in base")
        self.stdout.write(self.style.SUCCESS("Products created"))
