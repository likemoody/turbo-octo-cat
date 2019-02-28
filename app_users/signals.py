# User:     sender - what triggers the signal, what's sending the signal
# |     signal
# |     receiver - function that performs some task when signal is triggered
# Profile:  created by receiver

# User created >> signal triggered >> receiver creates a profile for newly created User

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
