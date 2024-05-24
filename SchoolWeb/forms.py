from django import forms

from .models import Home

class Post_Form(forms.ModelForm):

    class Meta:
        model = Home
        fields = ['Login_home', 'Courses', 'Feedback']