from django.shortcuts import render
from .models import Post,Profile,Comment
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django import forms
from .forms import PostForm, ProfileForm,CommentForm
from django.shortcuts import render, get_object_or_404
def home(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'blog/home.html',context)
def profile_detalis(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'blog/profile.html', context)
class AddblogView(CreateView):
    model=Post
    form_class=PostForm
    template_name='blog/create_post.html'
    success_url=reverse_lazy('home')
class AddProfile(CreateView):
    model=Profile
    form_class=ProfileForm
    template_name='blog/create_profile.html'
    success_url=reverse_lazy('profile')
class AddCommentsView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='blog/add_comment.html'
    #success_url=reverse_lazy('home')
    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('post_detail',kwargs={'pk':self.kwargs['pk']})
def comments_page(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'blog/comment.html',context)
def author_posts(request, id):
    profile = get_object_or_404(Profile, id=id)

    posts = Post.objects.filter(author=profile)

    return render(request, 'blog/author_posts.html', {
        'profile': profile,
        'posts': posts
    })