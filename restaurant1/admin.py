
from django.contrib import admin
from .models import Restaurant1, EmptyTables

class EmptyTablesInline(admin.TabularInline):
    model = EmptyTables
    extra = 1

class Restaurant1Admin(admin.ModelAdmin):
    inlines = [EmptyTablesInline]
admin.site.register(Restaurant1, Restaurant1Admin)