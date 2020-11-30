from django.db import models
from functools import reduce
from collections import Counter
import re

# Create your models here.


class Query(models.Model):
    name = models.CharField(max_length=128, blank=False)
    total_result = models.BigIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    client_ip = models.GenericIPAddressField()

    def __str__(self):
        return f'{self.name} found {self.created}'

    def get_popular_words(self):
        all_words = reduce((lambda a, b: a + b), [item['title'].split(
            ' ') + item['desc'].split(' ') for item in self.items.all().values('title', 'desc')])

        words_count = dict(Counter(filter(None, map(lambda word: re.sub(
            '[^A-Za-z0-9]+', '', word.lower()), all_words))))

        return sorted(words_count, key=words_count.get, reverse=True)[:10]


class Item(models.Model):
    position = models.IntegerField(blank=False)
    link = models.TextField()
    title = models.TextField()
    desc = models.TextField()
    query = models.ForeignKey(
        Query, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f'[{self.position}] {self.title}'
