from django import forms
from django.utils.translation import gettext as _
from .models import Comment, Post, Message


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title'  : _('Title'),
            'content': _('Content')
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title'  : '',
            'content': ''
        }

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['content'].required = False


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': ''
        }


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['user_to', 'content']
        labels = {
            'user_to': '',
            'content': '',
        }


class SendMessageToForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        labels = {
            'content': '',
        }
