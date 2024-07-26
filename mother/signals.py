from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Mother
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_mother(sender, instance, created, **kwargs):
    if created:
        user = instance
        mother = Mother.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name = user.first_name,
        )
