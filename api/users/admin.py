from django.contrib import admin
from api.users.models import CustomUser


admin.site.register(CustomUser)