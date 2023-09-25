from django import forms
from .models import Post,Category

choices = Category.objects.all().values_list('name','name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category','author', 'snippet','body')
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Write your title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title tag'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your blog snippet'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author', 'value':'', 'id': 'author', 'type':'hidden'}),
            'category': forms.Select(choices=choices,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Add your article....'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category','snippet','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title tag'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your blog snippet'}),
            'category': forms.Select(choices=choices,attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your article....'})
        }