from django.db import models
from django.db.models.signals import (post_save)
from django.contrib.auth.models import User
from django.dispatch import receiver
from django_countries.fields import CountryField


# USER PROFILE
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    country = CountryField(null=True, blank=True)
    # phone = models.IntegerField()
    city = models.CharField(max_length=100, null=True, blank=True)
    dp = models.ImageField(null=True, blank=True, default='placeholders/user/avatar-1577909.svg',
                           upload_to='user/profile/photos/')

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


# POST-REGISTRATION SIGNAL
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# POST-PROFILE-UPDATE SIGNAL
@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()
