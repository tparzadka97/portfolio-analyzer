from django.urls import path

from . import views

app_name = 'rate_my_portfolio'

urlpatterns = [
    path('', views.RateMyPortfolioView.as_view(), name='rate_my_portfolio'),
    path('post/create', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug>/edit', views.PostUpdateView.as_view(), name='post_edit'),
]
