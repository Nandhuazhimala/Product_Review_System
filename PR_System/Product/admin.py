from django.contrib import admin
from .models import *


# Register Products models

admin.site.register(Products)

# Regiser Review Models

admin.site.register(Review)