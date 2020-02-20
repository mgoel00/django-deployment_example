from django.contrib import admin
from django.contrib.auth.admin import User
from myapp.models import UserProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)
