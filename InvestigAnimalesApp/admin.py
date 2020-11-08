from django.contrib import admin
from .models import Animal

class animalAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
    list_display=["nombre", "especie", "created"]
    search_fields=["nombre"]
    list_filter=["especie"]

# Register your models here.
admin.site.register(Animal, animalAdmin)
