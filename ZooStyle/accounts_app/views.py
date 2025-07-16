from django.shortcuts import render, redirect

from django.urls import reverse_lazy

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login
from django.contrib import messages

from accounts_app.models import CustomUser
from accounts_app.forms import CustomUserCreationForm, CustomUserChangeForm

""" 
Custom User Registration 
"""
class SignUpView(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "accounts_app/signup.html"
    success_url = reverse_lazy('login')
    success_message = "Registration successful. Please log in."
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Unsuccessful registration. Invalid information.")
        return super().form_invalid(form)
    

""" 
Custom User Login 
"""
class SignInView(SuccessMessageMixin, LoginView):
    template_name = "accounts_app/signup.html"
    next_page = reverse_lazy('home')

    def get_success_url(self):
        messages.info(self.request, f"You are now logged in as {self.request.user.username}.")
        return super().get_success_url()
    
    
""" 
Custom User Logout 
"""
class CustomUserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, self.success_message)
        return response
    

""" 
Custom User Profile 
"""
class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'
    context_object_name = 'user'
    login_url = '/login/'

    def get_object(self):
        return self.request.user
    
""" 
Custom User Edit 
"""
class CustomUserUpdateView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('profile')
    success_message = "Profile updated successfully."
    
    def get_object(self):
        return self.request.user