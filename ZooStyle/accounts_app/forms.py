from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms

from django.utils.translation import gettext_lazy as _

from accounts_app.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = _("Пароль")
        self.fields['password1'].help_text = _("Пароль должен содержать как минимум 8 символов, не быть слишком простым или похожим на личную информацию.")
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'inputCreate', 'placeholder': _('* Придумайте пароль')})
        self.fields['password2'].label = _("Подтвердите пароль")
        self.fields['password2'].help_text = _("Повторите пароль для подтверждения.")
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'inputCreate', 'placeholder': _('* Повторите пароль')})
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['first_name', 'username',  'phone', 'address', 'pet_name']
        
        help_texts = {
            'first_name': '',
            'username': _('Не более 150 символов. Только буквы, цифры и символы (@ . + - _ )'),
            'phone': '',
            'address': _('Адрес проживания (необязательно).'),
            'pet_name': _('Имя вашего питомца (необязательно).'),
            }
        
        labels = {'photo': _('Фото профиля'),
            'first_name': _('Ваше Имя'),
            'username': _('Имя пользователя'),
            'phone': _('Номер телефона (+7(xxx) xxx-xx-xx)'),
            'address': _('Адрес'),
            'pet_name': _('Имя питомца'),
            }
        
        
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': _('* Введите ваше Имя')}),
            'username': forms.TextInput(attrs={'placeholder': _('* Придумайте себе уникальное имя пользователя')}),
            'phone': forms.TextInput(attrs={'placeholder': _('* Введите ваш номер телефона')}),
            'address': forms.TextInput(attrs={'placeholder': _('Введите ваш адрес')}),
            'pet_name': forms.TextInput(attrs={'placeholder': _('Введите имя вашего питомца')}),
        }
   
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['photo', 'username', 'first_name', 'phone', 'address', 'pet_name']
        
# class CustomAuthenticationForm(AuthenticationForm):
#     pass