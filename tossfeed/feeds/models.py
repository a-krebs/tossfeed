import datetime
import base64
from random import randint
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver


class Feed(models.Model):
    # token is a random number used as password to allow posting to feed
    _token = models.IntegerField(default=-1)
    _token_shown = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_posted = models.DateTimeField(auto_now=True)
    date_last_viewed = models.DateTimeField(default=datetime.datetime.now)
    views = models.IntegerField(default=0)

    @staticmethod
    @receiver(post_save)
    def set_token(sender, instance, created, raw, using, update_fields, *args, **kwargs):
        if sender is Feed and created:
            instance._token = randint(settings.FEED_TOKEN_MIN, settings.FEED_TOKEN_MAX)
            instance.save()

    @property
    def name(self):
        return str(self.id)

    @property
    def token(self):
        """
        The token should only ever be shown to the user once.
        """
        return str(self._token)
    
    @property
    def token_shown(self):
        if not self._token_shown:
            self._token_shown = True;
            self.save()
            return False
        return True

    #@staticmethod
    #def name_to_id(name):
    #    # length of string must be a multiple of 4 for decoding
    #    # if it's not, add '=' to the end to pad
    #    return base64.b32decode(str(name))

class Item(models.Model):
    feed = models.ForeignKey(Feed, related_name='items')
    date_posted = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
