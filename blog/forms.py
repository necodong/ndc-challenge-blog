from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class PromptForm(forms.Form):
    prompt = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
