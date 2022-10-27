from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):  # ModelForm -> 
    class Meta:
        model = Post
        fields = '__all__'

