from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from feeds import Feed as FeedModel

class TossFeed(Feed):
    def __init__(self, *args, **kwargs):
        self.feed = get_object_or_404(FeedModel, pk=kwargs.pop('feed_id', -1))
        self.title = self.feed.name
        self.link = reverse('feeds:index', feed_id=self.feed.id)
        self.description = 'TossFeed'
        super(TossFeed, self).__init__(*args, **kwargs)

    def items(self):
        return self.feed.objects.order_by('-date_posted')

    def item_title(self, item):
        return item.url

    def item_description(self, item):
        return item.url

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return item.url
