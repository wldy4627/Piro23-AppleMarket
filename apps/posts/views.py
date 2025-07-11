from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def main(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'posts/list.html', context=context)

def create(request):
    if request.method == 'GET':
        form = PostForm()
        context = { 'form': form }
        return render(request, 'posts/create.html', context=context)
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

def detail(request, pk):
    target_post = Post.objects.get(id = pk)
    context = { 'post': target_post }
    return render(request, 'posts/detail.html', context=context)

def update(request, pk):
    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        form = PostForm(instance=post)
        context = { 'form': form, 
                    'pk': pk }
        
        return render(request, 'posts/post_update.html', context=context)
    else:
        post = Post.objects.get(id=pk)
        form = PostForm(instance=post)
        if form.is_valid():
            form.save()
        return redirect(f'posts/detail/{pk}', pk)

def delete(request, pk):
    post = Post.Objects.get(id=pk)
    post.delete()
    return redirect('/')