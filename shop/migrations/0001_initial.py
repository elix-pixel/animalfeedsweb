from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=80)),
                ("slug", models.SlugField(blank=True, max_length=90, unique=True)),
                ("icon", models.CharField(blank=True, help_text="A single emoji shown next to the category, e.g. 🐔", max_length=10)),
                ("description", models.CharField(blank=True, max_length=200)),
                ("display_order", models.PositiveIntegerField(default=0)),
            ],
            options={
                "verbose_name_plural": "Categories",
                "ordering": ["display_order", "name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("unit", models.CharField(default="50kg bag", help_text="e.g. 50kg bag, 70kg bag, 2kg pack", max_length=40)),
                ("price", models.DecimalField(decimal_places=2, help_text="Price in KES. Update this any time stock prices change.", max_digits=10)),
                ("description", models.CharField(blank=True, max_length=200)),
                ("in_stock", models.BooleanField(default=True)),
                ("featured", models.BooleanField(default=False, help_text="Show this product near the top of its category.")),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="products", to="shop.category")),
            ],
            options={
                "ordering": ["category__display_order", "-featured", "name"],
            },
        ),
    ]
