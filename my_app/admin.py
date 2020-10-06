from django.contrib import admin
from .models import Search

class SearchAdmin(admin.ModelAdmin):
    list_display = ('city','search','created')
    list_filter=['created','city','search']

# Register your models here.
admin.site.register(Search, SearchAdmin)