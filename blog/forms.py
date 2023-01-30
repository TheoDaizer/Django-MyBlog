from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'post']
        error_mesages = {
            'title': {
                'required': 'Введите заголовок',
                'max_length': 'Превышена максимальная длина заголовка',
            },
            'description': {
                'required': 'Введите описание',
                'max_length': 'Превышена максимальная длина описания',
            },
            'post': {
                'required': 'Напишите пост!',
            },
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'post', 'autor']
