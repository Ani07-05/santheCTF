import uuid
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Challenge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    flag = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    flag_submitted = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    submission_time = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    unique_string = models.CharField(max_length=10, unique=True, default='')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        unique_string = uuid.uuid4().hex[:10]
        UserProfile.objects.create(user=instance, unique_string=unique_string)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
