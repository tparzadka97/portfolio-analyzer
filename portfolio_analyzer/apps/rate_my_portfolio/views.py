from django.contrib.auth import login, authenticate

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from portfolio_analyzer.apps.rate_my_portfolio.forms import PostCreateForm, PostUpdateForm
from portfolio_analyzer.apps.rate_my_portfolio.models import Post

from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseForbidden

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

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name='rate_my_portfolio/post_edit.html'
    model = Post
    form_class = PostUpdateForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().author:         
            return HttpResponseForbidden()

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('rate_my_portfolio:post_detail', kwargs={'slug': self.object.slug})