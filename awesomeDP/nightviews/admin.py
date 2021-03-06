from django.contrib import admin

from nightviews.models import Nightview

@admin.register(
    Nightview
)
class NightviewAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Nightview._meta.fields]