from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.db.models.signals import post_save





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwarg):
    if created:
        Profile.objects.create(user_id=instance)
