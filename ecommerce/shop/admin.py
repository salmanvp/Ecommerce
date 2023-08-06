from django.contrib import admin
from .import models
admin.site.register(models.category)
admin.site.register(models.Product)
