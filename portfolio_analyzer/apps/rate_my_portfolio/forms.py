from django import forms
from django.forms import fields

from portfolio_analyzer.apps.rate_my_portfolio.models import Post

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body']

class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body']
