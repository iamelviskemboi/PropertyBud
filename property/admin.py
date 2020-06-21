from django.contrib import admin

from .models import (Amenities, Property, Rating)

# Amenities
admin.site.register(Amenities)

# Property
admin.site.register(Property)

# Ratings
admin.site.register(Rating)
