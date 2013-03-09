from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from feeds import Feed as FeedModel

class TossFeed(Feed):
    title = "Chicagocrime.org site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to chicagocrime.org."
    def __init__(self, *args, **kwargs):
        self.feed = get_object_or_404(FeedModel, pk=kwargs.pop('feed_id', -1))
        self.title = self.feed.id
        super(TossFeed, self).__init__(*args, **kwargs)

    def items(self):
        return NewsItem.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('news-item', args=[item.pk])
