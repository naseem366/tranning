#from .models import add_category
from django.contrib.auth import models
from naseem.models import Category, Customer
from django.forms import ModelForm, fields
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm,SetPasswordForm,PasswordResetForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation

class CategoryForm(forms.ModelForm):
    name=forms.CharField(max_length=200)
    category_image=forms.ImageField()
    class Meta:
        model=Category
        fields="__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone','region','profile_pic','name']


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MyPasswordChangeForm(PasswordChangeForm):
	old_password=forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
	new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
	new_password2=forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))


class MyPasswordResetForm(PasswordResetForm):
	email=forms.EmailField(label=_("Email"),max_length=200,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))


class MySetPasswordForm(SetPasswordForm):
	new_password1 = forms.CharField(label=_("New password"),strip=False,
                                    widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
	new_password2= forms.CharField(label=_("New Password Confirmation"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
