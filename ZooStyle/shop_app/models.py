from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_("Category name"), max_length=120)
    description = models.TextField(_("Category description"), max_length=300, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    class UnitType(models.TextChoices):
        quantity = "Q", "шт"
        weight = "W", "гр"
    
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='products', verbose_name=_("Product category"))
    sku = models.CharField(_("SKU"), max_length=50, unique=True, blank=True)
    # slug = models.SlugField(_("Slug"), max_length=150, unique=True, blank=True)
    name = models.CharField(_("Product name"), max_length=120)
    description = models.TextField(_("Product description"), max_length=300, blank=True, null = True)
    price = models.DecimalField(_("Product price"), max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(_("Discount price"), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    unit_type = models.CharField(max_length=1, choices=UnitType.choices, default=UnitType.quantity, verbose_name=_("Product unit type"))
    units_in_stock = models.IntegerField(_("Product units in stock"), default=0)
    low_stock_threshold = models.IntegerField(_("Low stock threshold"), default=3)
    weight = models.FloatField(_("Product weight"), max_length=10, blank=True, null=True)
    manufacturer = models.CharField(_("Product manufacturer"), max_length=120, blank=True, null=True)
    average_rating = models.FloatField(_("Average rating"), default=0.0)
    image = models.ImageField(_("Product image"), upload_to='shop_app/products_photo/', default='shop_app/products_photo/default_product_pic.png')
    is_active = models.BooleanField(_("Product is active"), default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
