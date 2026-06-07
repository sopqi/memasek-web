
from django import forms
from .models import Comment, Mem, Like
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class MemForm(forms.ModelForm):
    class Meta:
        model = Mem
        fields = ['photo', 'title']


class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = [ ]

