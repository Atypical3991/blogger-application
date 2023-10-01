from django import forms
from .models import Post, Category, Profile, Comment

choices = Category.objects.all().values_list('name', 'name')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'header_image', 'category', 'author', 'snippet', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title tag'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your blog snippet'}),
            'author': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Author', 'value': '', 'id': 'author',
                       'type': 'hidden'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your article....'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'snippet', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title tag'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your blog snippet'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your article....'})
        }


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url', 'pinterest_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your bio'}),
            # 'profile_pic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title tag'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your website url'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your facebook url'}),
            'instagram_url': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Input your instagram url'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your twitter url'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your pinterest url'})
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your bio'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input your website url'}),
        }
