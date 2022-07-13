from django.db import models
from django.urls import reverse
from django.db.models import Q


# class models Category
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    def __str__(self):
        return self.name


# Class models for Subcategory
class Subcategory(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='category',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    def __str__(self):
        return self.name


# Class models for Product
class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory,
                                    related_name='products',
                                    on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    product_code = models.CharField(max_length=6, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer_date = models.DateTimeField(auto_now_add=True)
    owner_name = models.CharField(max_length=200, db_index=True)
    STATUS_ACTIVE = 'active'
    STATUS_CANCELLED = 'cancelled'
    STATUS_DRAFT = 'draft'
    STATUS_CHOICES = ((STATUS_ACTIVE, 'Active'),)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    # class Meta:
    #     ordering = ('name',)
    #     index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
