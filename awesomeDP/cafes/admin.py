from django.contrib import admin

from cafes.models import Cafe

@admin.register(
    Cafe
)
class CafeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Cafe._meta.fields]