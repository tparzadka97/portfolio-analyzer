from django.contrib.auth import login, authenticate

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from portfolio_analyzer.apps.accounts.forms import RegistrationForm, PortfolioCreateForm
from portfolio_analyzer.apps.accounts.models import Portfolio

from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404

import robin_stocks.robinhood as r

class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    success_message = "Your account was successfully created!"
    form_class = RegistrationForm

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name='accounts/profile.html'

class PortfolioView(LoginRequiredMixin, TemplateView):
    template_name='accounts/portfolio.html'
    
    def get(self, request, *args, **kwargs):
        context = {}
        portfolios = Portfolio.objects.filter(user=request.user)
        context['portfolios'] = portfolios
        return render(request, self.template_name, context)

    """
    def get(self, request, *args, **kwargs):
        login = r.login('', '', store_session=False)
        my_stocks = r.build_holdings()
        my_stock_tickers = list(my_stocks.keys())
        fundamentals = r.get_fundamentals(my_stock_tickers)
        
        for key,value in my_stocks.items():
            print(key,value)

        for key in fundamentals:
            print(key)

        return render(request, self.template_name, {'my_stocks': my_stocks})
    """

class PortfolioDetailView(LoginRequiredMixin, TemplateView):
    template_name='accounts/portfolio_detail.html'
    
    def get(self, request, slug):
        context = {}
        portfolio = get_object_or_404(Portfolio, slug=slug)
        context['portfolio'] = portfolio
        return render(request, self.template_name, context)

class PortfolioCreateView(LoginRequiredMixin, CreateView):
    template_name='accounts/portfolio_create.html'
    success_url = reverse_lazy('accounts:portfolio')
    success_message = "A new portfolio was successfully created!"
    form_class = PortfolioCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)