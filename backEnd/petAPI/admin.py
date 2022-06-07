from django.contrib import admin

from petAPI.models import Pet

admin.site.register(Pet)

class PetAdmin (admin.ModelAdmin):
    list_display = ('id', 'created', 'name', 'availability')

# Register your models here.
