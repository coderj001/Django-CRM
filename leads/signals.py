from django.db.models.signals import post_save
from django.dispatch import receiver

from leads.models import User, UserProfile


@receiver(post_save, sender=User)
def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
