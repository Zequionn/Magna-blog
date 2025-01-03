from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.

def home(request):
    posts = Post.objects.all()
    contexts = {'posts': posts}
    return render(request, 'Posts/posts_page.html', contexts)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request, 'Posts/post.html', context)


def form(request):
    post_form = PostForm()
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    context = {'form': post_form}
    return render(request, 'Posts/form_post.html', context)


def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    context = {'post': post}
    return render(request, 'Posts/delete_post.html', context)


def update_post(request, pk):
    post = Post.objects.get(id=pk)
    post_form = PostForm(instance=post)

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')

    context = {
        'form': post_form}
    return render(request, 'Posts/update_post.html', context)
