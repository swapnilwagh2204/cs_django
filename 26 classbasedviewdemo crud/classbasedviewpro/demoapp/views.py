from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class PostListView(ListView):
    #model = Post
    queryset = Post.objects.all()
    #context_object_name = 'post'
    template_name = 'demoapp/post_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['post'] = Post.objects.all()
        context['user'] = User.objects.all()
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    #fields = '__all__'
    success_url = '/demo/postlist/'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'obj'


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'demoapp/post_update.html'
    success_url = '/demo/postlist/'


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/demo/postlist/'