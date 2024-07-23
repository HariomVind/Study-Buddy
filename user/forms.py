from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models as user_model

class CreateUserForm(UserCreationForm):

    class Meta:
        model = user_model.User
        fields = ['first_name','last_name','email','username', "password1", "password2",'ucourse','ucollege']
        help_texts = {
            'username':None,
        }

class Addcollegeform(forms.ModelForm):

    class Meta:
        model = user_model.Usercollege
        fields = ['college',]

class Addcourseform(forms.ModelForm):

    class Meta:
        model = user_model.Usercourse
        fields = ['course',]