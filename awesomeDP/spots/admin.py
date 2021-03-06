from django.contrib import admin

from spots.models import Spot

@admin.register(
    Spot
)
class SpotAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Spot._meta.fields]