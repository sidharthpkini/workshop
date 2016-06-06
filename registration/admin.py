from django.contrib import admin

# Register your models here.
from django.contrib import admin
from registration.models import *

class ChocolateAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chocolate, ChocolateAdmin)

