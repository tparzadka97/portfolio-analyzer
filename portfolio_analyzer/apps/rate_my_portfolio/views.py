from django.contrib.auth import login, authenticate

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from portfolio_analyzer.apps.rate_my_portfolio.forms import PostCreateForm
from portfolio_analyzer.apps.rate_my_portfolio.models import Post

from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404

class RateMyPortfolioView(LoginRequiredMixin, TemplateView):
    template_name='rate_my_portfolio/forum.html'
    
    def get(self, request, *args, **kwargs):
        context = {}
        posts = Post.objects.all()
        context['posts'] = posts
        return render(request, self.template_name, context)

class PostDetailView(LoginRequiredMixin, CreateView):
    template_name='rate_my_portfolio/post_detail.html'
    
    def get(self, request, slug):
        context = {}
        post = get_object_or_404(Post, slug=slug)
        context['post'] = post
        return render(request, self.template_name, context)

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name='rate_my_portfolio/post_create.html'
    success_url = reverse_lazy('rate_my_portfolio:rate_my_portfolio')
    success_message = "A new post was successfully created!"
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
