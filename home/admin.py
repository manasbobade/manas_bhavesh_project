from django.contrib import admin
from home.models import Contact
from . import models
# Register your models here.
admin.site.register(Contact)
admin.site.register(models.Question)
admin.site.register(models.Response)