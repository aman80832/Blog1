from django import forms
from .models import Post,Profile,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name','education','age']
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','text','post']