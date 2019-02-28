from PIL import Image
from django.contrib.auth.models import User
from django.db import models

from toc.utils import MediaFiles


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to=MediaFiles.upload_path)
    description = models.TextField(max_length=150, null=True)
    blocked = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'Profile({self.user.username})'
