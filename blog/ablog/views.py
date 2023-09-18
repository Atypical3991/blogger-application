from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm

# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = "home.html"

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddArticle(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_blog.html'
    # fields = '__all__'

class UpdateArticle(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_blog.html'

class DeleteArticle(DeleteView):
    model = Post
    form_class = EditForm
    template_name = 'update_blog.html'