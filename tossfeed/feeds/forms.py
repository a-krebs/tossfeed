from django import forms
from feeds.models import Feed, Item

class CreateFeedForm(forms.Form):
    url = forms.URLField(label='')

    def create_feed(self):
        f = Feed.objects.create()
        i = Item.objects.create(feed=f,url=self.cleaned_data['url'])
        return f

