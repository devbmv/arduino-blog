from .models import Comment, ProjectPost
from .forms import CommentForm, ProjectPostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse


def my_blog(request):
    return HttpResponse("Hello, Blog!")


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
