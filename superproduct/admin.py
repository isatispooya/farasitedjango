from django.contrib import admin
from . import models
admin.site.register(models.SubSuperProduct)
admin.site.register(models.SuperProduct)