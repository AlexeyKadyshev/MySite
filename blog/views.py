from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from blog.forms import UserForm, AddPost
from blog.models import User, Post


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['name']
            users = User.objects.all()
            if user_name not in users:
                user = User(user_name=user_name)
                user.save()
                return redirect('about')
            return redirect('about')
    form = UserForm()
    return render(request, 'blog/index.html', {'form': form})


def about(request):
    return render(request, 'blog/about.html')


def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts})


def write_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/good_post.html')
        return render(request, 'blog/index.html')
    form = AddPost()
    return render(request, 'blog/write_post.html', {'form': form})


def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return render(request, 'blog/bad_post.html')
    except Post.DoesNotExist:
        return HttpResponseNotFound('<h2>Кто-то уже это сделал!!!</h2>')
