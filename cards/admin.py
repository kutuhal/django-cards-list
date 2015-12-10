from django.contrib import admin
#Importing the Cards model
from .models import Cards, UserProfile

# Register your models here.
admin.site.register(Cards) # Doing this will ensure that the Cards Model is shown in Admin
admin.site.register(UserProfile)