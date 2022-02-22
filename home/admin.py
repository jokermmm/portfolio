from dataclasses import fields
from django.contrib import admin

from home.models import Data

class DataAdmin(admin.ModelAdmin):
    # fields = (('name','title'), 'phone_number')
    list_display = ['name','title','phone_number']

admin.site.register(Data, DataAdmin)
# Register your models here.
