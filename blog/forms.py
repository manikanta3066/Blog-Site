from django import forms
from .models import Post
# PostForm is a Django ModelForm -> It automatically creates form fields based on our Post model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # This tells Django to use the Post model for the form
        fields = ['title', 'content']  # These fields will be shown in the form