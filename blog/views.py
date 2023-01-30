from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import AddPostForm, EditPostForm
from .models import Post


class BlogView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog.html'


class DetailPostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail_post.html'


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'blog/add_post.html'
#    success_url = '/'


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'blog/add_post.html'
