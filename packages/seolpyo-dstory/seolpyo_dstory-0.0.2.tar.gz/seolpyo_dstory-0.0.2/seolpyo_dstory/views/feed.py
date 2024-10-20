from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.contrib.syndication.views import Feed
from django.shortcuts import resolve_url
from django.utils import timezone
from django.utils.feedgenerator import Rss201rev2Feed

from bs4 import BeautifulSoup

from .. import settings as dstory_setting
from ..models import Post


class FeedType(Rss201rev2Feed):
    content_type = 'application/xml; charset=utf-8'


class FeedView(Feed):
    title = getattr(settings, 'DSTORY_CONTEXT', {}).get('site_name', '디스토리') + ' RSS'
    description = 'This site engiened Django.'
    feed_type = FeedType
    limit = getattr(settings, 'DSTORY_RSS', dstory_setting.DSTORY_RSS)

    def link(self): return resolve_url('seolpyo_dstory:list')

    def items(self): return Post.objects.filter(is_private=False, date_pub__lte=timezone.now())

    def item_description(self, obj: Post):
        if obj.password: return '비밀 글입니다.'
        return obj.text

    def item_pubdate(self, obj: Post): return timezone.localtime(obj.date_pub)

    def item_author_name(self, obj: Post): return obj.author

    def item_link(self, obj: Post): return obj.get_absolute_url()
    item_guid_is_permalink = not getattr(settings, 'DSTORY_SLUG', False)


class BlogSitemap(Sitemap):
    priority = 0.6
    limit = 9999
    def items(self): return Post.objects.filter(is_private=False, date_pub__lte=timezone.now())

    def lastmod(self, obj: Post): return timezone.localtime(obj.date_pub)

sitemaps = {'sitemaps': {'tistory': BlogSitemap}, 'template_name': 'seolpyo_dstory/sitemap.html'}