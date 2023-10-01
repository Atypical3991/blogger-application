"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddArticle, UpdateArticle,DeleteArticle,AddCategory,CategoryView,CategoryListView,LikeView,ShowProfilePageView,EditProfilePageView,CreateProfilePageView,AddCommentView
urlpatterns = [
    # path('', views.home, name='home')
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('article/', AddArticle.as_view(), name='add-article'),
    path('article/edit/<int:pk>', UpdateArticle.as_view(), name='article-edit'),
    path('category/',  AddCategory.as_view(), name='add-category'),
    path('article/delete/<int:pk>', DeleteArticle.as_view(), name='article-delete'),
    path('category/<str:cat>', CategoryView, name='show-posts-by-category'),
    path('category_list/', CategoryListView, name='category-list'),
    path('like/<int:pk>',  LikeView, name='like_post'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='profile'),
    path('<int:pk>/edit_profile', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('/create_profile', CreateProfilePageView.as_view(), name='create_profile_page'),
    path('/article/<int:pk>/add_comment', AddCommentView.as_view(), name='add_comment')

]
