from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# def home(request):
#     return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-blog_date']

    def get_context_data(self,*args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        context["total_likes"] = post.get_total_likes()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["liked"] = liked
        return context

class AddArticle(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_blog.html'
    # fields = '__all__'

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddArticle, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

class UpdateArticle(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_blog.html'

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdateArticle, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

class DeleteArticle(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeleteArticle, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategory, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request,cat):
    category_posts = Post.objects.filter(category=cat.replace('-',' '))
    return render(request,'category.html',{'cat':cat.title().replace('-',' '), 'category_posts':category_posts, 'cat_menu':Category.objects.all()})

def CategoryListView(request):
    category_list = Category.objects.all()
    return render(request,'category_list.html',{'category_list': category_list})

def LikeView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        liked = True
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))