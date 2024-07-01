
from django import forms
from .models import ProjectPost


class ProjectPostForm(forms.ModelForm):
    class Meta:
        model = ProjectPost
        fields = ['title', 'content']
