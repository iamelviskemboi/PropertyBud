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

    # photo upload directory
    def profile_directory_path(self, user):
        return 'photos/Accounts/UserProfiles/{1}'.format(user=self.user.email)

    dp = models.ImageField(upload_to=profile_directory_path, default='placeholders/user/avatar-1577909.svg', blank=True, null=True)

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


# OWNER PROFILE
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=90)
    city = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    facebook = models.URLField(blank=True, null=True, unique=True)
    twitter = models.URLField(blank=True, null=True, unique=True)
    linkedin = models.URLField(blank=True, null=True, unique=True)
    youtube = models.URLField(blank=True, null=True, unique=True)
    website = models.URLField(blank=True, null=True, unique=True)
    address = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)

    # photo upload directory
    def owner_directory_path(self, owner):
        return 'photos/Accounts/OwnerProfiles/{1}'.format(owner=self.email)

    dp = models.ImageField(upload_to=owner_directory_path, default='placeholders/user/avatar-1577909.svg')

    def __str__(self):
        return self.name.upper()
