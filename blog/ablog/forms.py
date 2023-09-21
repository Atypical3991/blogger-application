from django import forms
from .models import Post,Category

choices = Category.objects.all().values_list('name','name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','author', 'body')
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Write your title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title tag'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Add your article....'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title tag'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your article....'})
        }