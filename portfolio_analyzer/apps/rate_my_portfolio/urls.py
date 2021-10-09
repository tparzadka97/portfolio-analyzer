from django.urls import path

from . import views

app_name = 'rate_my_portfolio'

urlpatterns = [
    path('', views.RateMyPortfolioView.as_view(template_name="rate_my_portfolio/forum.html"), name='rate_my_portfolio'),
    path('post/create', views.PostCreateView.as_view(template_name="rate_my_portfolio/post_create.html"), name='post_create'),
    path('post/<slug>', views.PostDetailView.as_view(template_name="rate_my_portfolio/post_detail.html"), name='post_detail'),
]
