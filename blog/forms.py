
from .models import Comment
from django import forms
from .models import ProjectPost


class ProjectPostForm(forms.ModelForm):
    class Meta:
        model = ProjectPost
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


