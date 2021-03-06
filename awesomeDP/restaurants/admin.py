from django.contrib import admin

from restaurants.models import Restaurant

@admin.register(
    Restaurant
)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Restaurant._meta.fields]