from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Items, Profile
from django.db.models.signals import post_save , pre_save
from django.utils.text import slugify





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwarg):
    if created:
        Profile.objects.create(user_id=instance)

