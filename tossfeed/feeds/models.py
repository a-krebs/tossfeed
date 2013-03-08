import datetime
from django.db import models


class Feed(models.Model):
    token = models.IntegerField()
    date_created = models.DateFieldTimeField(auto_now_add=True)
    date_last_posted = models.DateTimeField(auto_now=True)
    date_last_viewed = models.DateTimeField(default=datetime.now)
    views = models.IntegerField(default = 0)

class Item(models.Model):
    feed = models.ForeignKey(Feed, related_name='items')
    date_posted = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
