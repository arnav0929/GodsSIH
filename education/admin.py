from django.contrib import admin

# Register your models here.
from .models import users,Jobs

admin.site.register(users)
admin.site.register(Jobs)