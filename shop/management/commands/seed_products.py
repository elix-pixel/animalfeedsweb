from django.core.management.base import BaseCommand

from shop.models import Category, Product


CATEGORIES = [
    {"name": "Poultry Feed", "icon": "🐔", "display_order": 1,
     "description": "Chick mash to layers mash, for every stage."},
    {"name": "Dairy & Livestock", "icon": "🐄", "display_order": 2,
     "description": "Dairy meal and mineral supplements."},
    {"name": "Pig Feed", "icon": "🐖", "display_order": 3,
     "description": "Starter through to finisher rations."},
    {"name": "Rabbit Feed", "icon": "🐇", "display_order": 4,
     "description": "Pelleted feed for growing and breeding rabbits."},
    {"name": "Pet Food", "icon": "🐕", "display_order": 5,
     "description": "Dog and cat meal for home and working animals."},
]

# NOTE: prices below are placeholders so the site has something to display.
# Replace them with your real, current prices via /admin — they are not
# live market data.
PRODUCTS = [
    ("Poultry Feed", "Chick Mash", "50kg bag", 2900, True),
    ("Poultry Feed", "Growers Mash", "50kg bag", 2800, False),
    ("Poultry Feed", "Layers Mash", "50kg bag", 2750, True),
    ("Poultry Feed", "Broiler Starter", "50kg bag", 3100, False),
    ("Poultry Feed", "Broiler Finisher", "50kg bag", 3000, False),
    ("Dairy & Livestock", "Dairy Meal", "70kg bag", 3400, True),
    ("Dairy & Livestock", "Calf Pellets", "50kg bag", 3200, False),
    ("Dairy & Livestock", "Mineral Supplement", "5kg pack", 950, False),
    ("Pig Feed", "Pig Starter", "50kg bag", 3300, False),
    ("Pig Feed", "Pig Grower", "50kg bag", 3150, False),
    ("Pig Feed", "Pig Finisher", "50kg bag", 3050, True),
    ("Rabbit Feed", "Rabbit Pellets", "25kg bag", 1700, True),
    ("Pet Food", "Dog Meal", "10kg bag", 1450, True),
]


class Command(BaseCommand):
    help = "Populate the database with sample categories and products."

    def handle(self, *args, **options):
        cat_lookup = {}
        for c in CATEGORIES:
            obj, created = Category.objects.update_or_create(
                name=c["name"],
                defaults={
                    "icon": c["icon"],
                    "display_order": c["display_order"],
                    "description": c["description"],
                },
            )
            cat_lookup[c["name"]] = obj
            self.stdout.write(
                self.style.SUCCESS(f"{'Created' if created else 'Updated'} category: {obj.name}")
            )

        for cat_name, name, unit, price, featured in PRODUCTS:
            obj, created = Product.objects.update_or_create(
                name=name,
                category=cat_lookup[cat_name],
                defaults={
                    "unit": unit,
                    "price": price,
                    "featured": featured,
                    "in_stock": True,
                },
            )
            self.stdout.write(
                self.style.SUCCESS(f"{'Created' if created else 'Updated'} product: {obj.name}")
            )

        self.stdout.write(self.style.SUCCESS("\nDone. Sample data loaded."))
        self.stdout.write(
            "Remember: these prices are placeholders — edit them at /admin "
            "to match what you actually charge."
        )
