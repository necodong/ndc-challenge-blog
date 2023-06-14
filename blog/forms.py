from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'thumbnail')

class PromptForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'prompt', 'image_prompt')
