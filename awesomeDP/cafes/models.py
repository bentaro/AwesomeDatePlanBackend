from django.db import models
import uuid

class Cafe(models.Model):
    class Meta:
        db_table = 'cafe'
    
    cafe_id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=132, blank=False, null=False)
    picture = models.URLField(blank=False, null=False)
    detail_url = models.URLField(blank=False, null=False)
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
