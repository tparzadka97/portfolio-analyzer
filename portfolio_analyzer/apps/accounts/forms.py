from django import forms
from django.contrib.auth.forms import UserCreationForm

from portfolio_analyzer.apps.accounts.models import Account, Portfolio

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

class PortfolioCreateForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ('name', 'description')