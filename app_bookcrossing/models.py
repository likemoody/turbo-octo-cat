from django.contrib.auth.models import User
from django.db import models
from toc.utils import MediaFiles


class Book(models.Model):
    title = models.TextField(max_length=60)
    author = models.TextField(max_length=60)
    year = models.PositiveIntegerField()

    publisher = models.TextField(max_length=60)
    description = models.TextField(max_length=60)

    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='book_owners')

    cover_img = models.FileField(default='default_book_cover.jpg', upload_to=MediaFiles.upload_path)

    is_booked = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return f'Book "{self.title}" by {self.author} ({self.year})'
