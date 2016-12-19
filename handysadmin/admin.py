from django.contrib import admin
from .models import *

admin.site.register(AdminUser)
admin.site.register(User)
admin.site.register(UserType)
admin.site.register(UserAreaType)
