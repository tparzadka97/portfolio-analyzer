from django.urls import path

from . import views

app_name = 'rate_my_portfolio'

urlpatterns = [
    path('', views.rate_my_portfolio, name='rate_my_portfolio'),
    path('create/', views.rate_my_portfolio, name='create')
]
