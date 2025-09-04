from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid

from shop_app.models import Product

@receiver(pre_save, sender = Product)
def generate_product_sku(sender, instance, **kwargs):
    if not instance.sku:
        instance.sku = str(uuid.uuid4()).replace("-", "")[:10].upper()
    