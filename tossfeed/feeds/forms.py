from django import forms

class CreateFeedForm(forms.Form):
    url = forms.URLField()

    def create_feed(self):
        f = Feed.objects.create()
        i = Item.objects.create(feed=f,url=self.cleaned_data['url'])
        return f

