from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('portfolio', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio/create', views.PortfolioCreateView.as_view(template_name="accounts/portfolio_create.html"), name='portfolio_create'),
    path('portfolio/<slug>', views.PortfolioDetailView.as_view(template_name="accounts/portfolio_detail.html"), name='portfolio_detail'),
    path('login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterView.as_view(template_name="registration/register.html"), name='register'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done'), template_name='registration/password_change.html'), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
