from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Users)
admin.site.register(Items)
admin.site.register(UsersRentedItems)
admin.site.register(UsersRequestedItems)
