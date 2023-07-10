from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SigninForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
class SignupForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['first_name','last_name','email','username','password1','password2']
        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}),
            'email'     : forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}),
            'username'  : forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}),
        }
        
class TodoForms(forms.ModelForm):
    class Meta:
        model  = Todoo
        fields = ['title','description']
        widgets = {
            'title':forms.TextInput(attrs={'placeholder':"Title",'class':'form-control'}),
            'description':forms.Textarea(attrs={'placeholder':"Description",'class':'form-control'})
        }
