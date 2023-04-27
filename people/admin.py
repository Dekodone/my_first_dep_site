from django.contrib import admin
from .models import person

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","emale","phone","age")

admin.site.register(person, PersonAdmin)