# blog/views.py

from django.shortcuts import render, redirect
from .forms import ProjectPostForm
from django.contrib.auth.decorators import login_required

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
