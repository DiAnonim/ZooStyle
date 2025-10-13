from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_("Category name"), max_length=120)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name='children', verbose_name=_("Parent category"), blank=True, null=True)
    level_view = models.IntegerField(_("Category level view"), default=1)
    
    def __str__(self):
        return self.get_full_path()
    
    def get_full_path(self):
        path_parts = [self.name]
        current_parent = self.parent
        while current_parent:
            path_parts.insert(0, current_parent.name)
            current_parent = current_parent.parent
        return "/".join(path_parts)
    
    def get_level_view(self):
        path = self.get_full_path()
        return int(path.count("/")) + 1 
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
        
class Tag(models.Model):
    name = models.CharField(_("Tags name"), max_length=120)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    class UnitType(models.TextChoices):
        quantity = "Q", "шт"
        weight = "W", "кг"
    
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='products', verbose_name=_("Product category"))
    tags = models.ManyToManyField(to=Tag, related_name='products', blank=True, verbose_name=_("Product tags"))

    sku = models.CharField(_("SKU"), max_length=50, unique=True, blank=True)

    name = models.CharField(_("Product name"), max_length=120)
    description = models.TextField(_("Product description"), max_length=300, blank=True, null = True)
    price = models.DecimalField(_("Product price"), max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(_("Discount price"), max_digits=10, decimal_places=2, blank=True, null=True, default=0)
    manufacturer = models.CharField(_("Product manufacturer"), max_length=120, blank=True, null=True)
    image = models.ImageField(_("Product image"), upload_to='shop_app/products_photo/', default='shop_app/products_photo/default_product_pic.png')

    unit_type = models.CharField(_("Product unit type"), max_length=1, choices=UnitType.choices, default=UnitType.quantity)
    quantity_in_stock = models.IntegerField(_("Product quantity in stock"), default=0)
    weight_in_stock  = models.DecimalField(_("Product weight in stock"), max_digits=10, decimal_places=3, blank=True, null=True)

    average_rating = models.FloatField(_("Average rating"), default=0.0)
    is_active = models.BooleanField(_("Product is active"), default=False)
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
