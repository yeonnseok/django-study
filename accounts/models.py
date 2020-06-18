from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="member")
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    @receiver(post_save, sender=User)
    def create_user_member(sender, instance, created, **kwargs):
        if created:
            Member.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_member(sender, instance, **kwargs):
        instance.member.save()
