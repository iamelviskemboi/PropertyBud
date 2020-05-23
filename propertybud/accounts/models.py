from django.db import models
from django.contrib.auth.models import User


# USER PROFILE
class Profile(models.Model):
    COUNTRIES = (
        ('Kenya', 'KENYA'),
        ('mexico', 'MEXICO'),
        ('U.S.A', 'U.S.A'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, choices=COUNTRIES, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    dp = models.ImageField(null=True, blank=True, default='placeholders/user/alaska-4714097_1920.jpg', upload_to='user/profile/photos/')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
