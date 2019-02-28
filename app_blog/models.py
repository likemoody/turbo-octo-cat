from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
from django.urls.base import reverse


class Post(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    blocked = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    # last_edited_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('blog-home')

    def __str__(self):
        return f'Post({self.title})'


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='post_comments')
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment({self.post})'


class Message(models.Model):
    content = models.TextField(max_length=60)
    date_sent = models.DateTimeField(default=timezone.now)
    date_read = models.DateTimeField(default=timezone.now, null=True)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='messages_sent')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='messages_received')
    is_read = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f'Message({self.user_from} > {self.user_to})'
