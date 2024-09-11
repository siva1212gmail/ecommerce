from django.core.management.base import BaseCommand
from eapp.models import Products  # Import your Products model
import random
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the Products model with 100 dummy products'

    def handle(self, *args, **kwargs):
        fake = Faker()
        categories = ['Electronics', 'Clothing', 'Books', 'Home & Kitchen', 'Sports']
        subcategories = ['New Arrivals', 'Best Sellers', 'Discounts', 'Featured']

        for _ in range(100):
            product_name = fake.word()
            category = random.choice(categories)
            subcategory = random.choice(subcategories)
            price = random.randint(1, 1000)
            description = fake.text(max_nb_chars=100)
            # Replace `image_path` with a path to a dummy image or use a placeholder image URL
            image_path = 'images/images/dummy_image.jpg'

            Products.objects.create(
                product_Name=product_name,
                category=category,
                subcatagory=subcategory,
                price=price,
                desc=description,
                images=image_path
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product_name}'))