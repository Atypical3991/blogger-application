from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-blog_date']

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
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')

class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')