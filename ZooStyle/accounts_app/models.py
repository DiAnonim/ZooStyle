from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from accounts_app.validators import validate_phone_number

class CustomUser(AbstractUser):
    name = models.CharField(_("Name"), max_length=150)
    phone = models.CharField(_("Phone number"), max_length=20, validators=[validate_phone_number])
    address = models.CharField(_("Address"), max_length=255, blank=True, null=True)
    photo = models.ImageField(_("Photo"), upload_to='profile_photo/', blank=True, null=True)
    pet_name = models.CharField(_("Pet name"), max_length=100, blank=True, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["name", "phone"]
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
