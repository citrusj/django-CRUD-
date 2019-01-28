from django.shortcuts import render
from .models import Post
from django.utils import timezone
from . forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html',{'posts':posts})
    
def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/post_detail.html',{'post':post})
    
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})
    
def post_edit(request, post_id):
    post = Post.objects.get(pk = post_id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html',{'form':form})
    
def post_delete(request, post_id):
    post = Post.objects.get(pk = post_id)
    post.delete()
    return redirect('post_list')
    