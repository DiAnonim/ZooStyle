from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms

from accounts_app.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['photo', 'username', 'name', 'phone', 'address', 'pet_name']
        
        labels = {'photo': '',
                  'username': '',
                  'name': '',
                  'phone': '',
                  'address': '',
                  'pet_name': ''}
        
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Имя'}),
        #     'last_name': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Фамилия'}),
        #     'email': forms.EmailInput(attrs={'class': 'inputCreate', 'placeholder': 'Email'}),
        #     'username': forms.TextInput(attrs={'class': 'inputCreate', 'placeholder': 'Username/Логин'}),
        # } 
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['photo', 'username', 'name', 'phone', 'address', 'pet_name']
        
# class CustomAuthenticationForm(AuthenticationForm):
#     pass