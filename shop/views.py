from django.shortcuts import render

from .models import Category


def home(request):
    """Single-page storefront: shop info plus every category and its products."""
    categories = (
        Category.objects.prefetch_related("products")
        .all()
        .order_by("display_order", "name")
    )
    return render(request, "shop/home.html", {"categories": categories})
