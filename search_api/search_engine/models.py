from django.db import models

# Create your models here.


class Query(models.Model):
    name = models.CharField(max_length=128, blank=False)
    total_result = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


class Item(models.Model):
    position = models.IntegerField(blank=False)
    link = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    desc = models.TextField()
    query = models.ForeignKey(
        Query, on_delete=models.CASCADE, related_name='items')
