from django import forms
from .models import Profiles, Comments, Images
from django.contrib.auth.forms import AuthenticationForm

class PostImagesForm(forms.ModelForm):
    image = forms.ImageField()
    caption = forms.CharField(max_length=100)
    class Meta: 
        model = Images
        exclude = ['posted','profile']
        
        
class PostComment(forms.ModelForm):
    class Meta: 
        model = Comments
        exclude = ['image','posted','user']

class PostProfile(forms.ModelForm):
    class Meta:
        models = Profiles
        exclude = ['user',]
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder':'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'Password'
        }
    ))
        