from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """A feed category, e.g. Poultry Feed, Dairy & Livestock."""

    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=90, unique=True, blank=True)
    icon = models.CharField(
        max_length=10,
        blank=True,
        help_text="A single emoji shown next to the category, e.g. 🐔",
    )
    description = models.CharField(max_length=200, blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["display_order", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    """A single feed product sold in the shop."""

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=120)
    unit = models.CharField(
        max_length=40,
        default="50kg bag",
        help_text="e.g. 50kg bag, 70kg bag, 2kg pack",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Price in KES. Update this any time stock prices change.",
    )
    description = models.CharField(max_length=200, blank=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(
        default=False, help_text="Show this product near the top of its category."
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category__display_order", "-featured", "name"]

    def __str__(self):
        return f"{self.name} ({self.unit})"
