from django.contrib import admin
from home.models import Contact
from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import User
# Register your models here.
admin.site.register(Contact)
admin.site.register(models.Question)
admin.site.register(models.Response)
