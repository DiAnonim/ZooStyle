from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid

from shop_app.models import Product, Category

@receiver(pre_save, sender = Product)
def generate_product_sku(sender, instance, **kwargs):
    if not instance.sku:
        instance.sku = str(uuid.uuid4()).replace("-", "")[:10].upper()
        
        
@receiver(pre_save, sender = Category)
def add_category_level_view(sender, instance, **kwargs):
    instance.level_view = instance.get_level_view()
    