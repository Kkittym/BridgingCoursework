from django import forms
from django.forms import Textarea
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'text': Textarea(attrs={'cols':80, 'rows':2})
        }