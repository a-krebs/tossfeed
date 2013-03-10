from django import forms
from feeds.models import Feed, Item

class CreateFeedForm(forms.Form):
    url = forms.URLField(label='')

    def create_feed(self):
        f = Feed.objects.create()
        _ = Item.objects.create(feed=f,url=self.cleaned_data['url'])
        return f

class AddToFeedForm(forms.Form):
    url = forms.URLField(label='URL')
    token = forms.IntegerField(label='Password')
    
    def add_to_feed(self, feed):
        """
        Make a new Item and add it to the feed given.
        
        Returns the new item, or None if the token is incorrect.
        """
        if self.cleaned_data['token'] == feed.token:
            i = Item.objects.create(feed=feed,url=self.cleaned_data['url'])
            return i
        else:
            return None