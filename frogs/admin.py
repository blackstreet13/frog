from django.contrib import admin
from .models import Frogs
# Register your models here.
class FrogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'color', 'year')
    search_fields = ('name',)
    list_filter = ('name',)
admin.site.register(Frogs, FrogAdmin)
