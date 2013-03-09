import datetime
import base64
from random import randint
from django.db import models


class Feed(models.Model):
    token = models.IntegerField(default=-1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_posted = models.DateTimeField(auto_now=True)
    date_last_viewed = models.DateTimeField(default=datetime.date.today)
    views = models.IntegerField(default=0)

    @property
    def name(self):
        return base64.b32encode(str(self.id))

    @staticmethod
    def name_to_id(name):
        # length of string must be a multiple of 4 for decoding
        # if it's not, add '=' to the end to pad
        return base64.b32decode(str(name))

    def save(self, *args, **kwargs):
        if self.token == -1:
            # token has not been set
            self.token = randint(2,1000000)
            super(Feed, self).save(*args, **kwargs)

class Item(models.Model):
    feed = models.ForeignKey(Feed, related_name='items')
    date_posted = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
