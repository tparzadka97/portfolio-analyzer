from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render

import robin_stocks.robinhood as r

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name='accounts/profile.html'

class PortfolioView(LoginRequiredMixin, TemplateView):
    template_name='accounts/portfolio.html'

    def get(self, request, *args, **kwargs):
        login = r.login('', '')
        my_stocks = r.build_holdings()
        my_stock_tickers = list(my_stocks.keys())
        fundamentals = r.get_fundamentals(my_stock_tickers)
        
        for key,value in my_stocks.items():
            print(key,value)

        for key in fundamentals:
            print(key)

        return render(request, self.template_name, {'my_stocks': my_stocks})