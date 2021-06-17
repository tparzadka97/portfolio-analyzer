from django.shortcuts import redirect, render

def rate_my_portfolio(request):
    return render(request, 'rate_my_portfolio/forum.html')