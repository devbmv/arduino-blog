# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import ProjectPost, Comment
from .forms import ProjectPostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    project_posts = ProjectPost.objects.all()
    paginator = Paginator(project_posts, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})

def post_detail(request, post_id):
    post = get_object_or_404(ProjectPost, id=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

@login_required
def create_project_post(request):
    if request.method == 'POST':
        form = ProjectPostForm(request.POST)
        if form.is_valid():
            project_post = form.save(commit=False)
            project_post.author = request.user
            project_post.save()
            return redirect('index')
    else:
        form = ProjectPostForm()
    return render(request, 'blog/create_project_post.html', {'form': form})

@login_required
def edit_project_post(request, post_id):
    post = get_object_or_404(ProjectPost, id=post_id)
    if request.method == 'POST':
        form = ProjectPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = ProjectPostForm(instance=post)
    return render(request, 'blog/edit_project_post.html', {'form': form})

@login_required
def delete_project_post(request, post_id):
    post = get_object_or_404(ProjectPost, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, 'blog/delete_project_post.html', {'post': post})
