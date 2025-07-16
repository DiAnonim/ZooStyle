import phonenumbers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone_number(value):
    try:
        number = phonenumbers.parse(value, "RU")
        if not phonenumbers.is_valid_number(number):
            raise ValidationError(_("Invalid phone number."))
    except phonenumbers.phonenumberutil.NumberParseException:
        raise ValidationError(_("Invalid phone number format."))