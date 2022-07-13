from django.contrib import admin
from .models import *


# Register your models here.


# admin.site.register(Category)
# admin.site.register(Subcategory)
# admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "name", "slug")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "product_code", "price",
                    "manufacturer_date", "owner_name", "status")
