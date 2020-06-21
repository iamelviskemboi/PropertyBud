from django.db import models
from django.contrib.auth.models import User

from accounts.models import Owner


# CHOICES
PROPERTIES = (
    ('flat', 'Flat'),
    ('apartment', 'Apartment'),
    ('condominium', 'Condo'),
    ('single', 'Single'),
    ('self', 'Self'),
    ('bedsitter', 'Bedsitter'),
)

RATINGS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

TRANSACTIONS = (
    ('sale', 'FOR SALE'),
    ('rent', 'FOR RENT'),
)


# Rating
class Rating(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField(choices=RATINGS)

    def __str__(self):
        return self.name


# Amenities
class Amenities(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Amenities'

    def __str__(self):
        return self.name


# Property
class Property(models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=3299)
    transaction = models.CharField(max_length=10, choices=TRANSACTIONS, default='sale')
    property_type = models.CharField(max_length=50, choices=PROPERTIES)
    rooms = models.PositiveSmallIntegerField()
    is_verified = models.BooleanField(default=False)
    is_sponsored = models.BooleanField(default=False)
    is_furnished = models.BooleanField()
    is_featured = models.BooleanField(default=False)
    amenities = models.ForeignKey(Amenities, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    photo_1 = models.ImageField(upload_to='listing')
    photo_2 = models.ImageField(upload_to='listing')
    photo_3 = models.ImageField(upload_to='listing')
    photo_4 = models.ImageField(upload_to='listing')
    photo_5 = models.ImageField(upload_to='listing')

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.title
