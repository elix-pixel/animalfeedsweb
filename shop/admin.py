from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "display_order")
    list_editable = ("display_order",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("display_order", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "unit", "price", "in_stock", "featured", "updated_at")
    list_editable = ("price", "in_stock", "featured")
    list_filter = ("category", "in_stock", "featured")
    search_fields = ("name", "description")
    ordering = ("category", "name")
