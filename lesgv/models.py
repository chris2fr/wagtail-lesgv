from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import  FieldPanel, MultiFieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)
import lesgv.services
from lesgv.blocks import GhostIndexBlock

# from django.urls import reverse
# from django.contrib.syndication.views import Feed
# from django.template.defaultfilters import truncatewords
# from django.contrib.auth import get_user_model

# from puput.models import EntryPage, BlogPage


# class FeedMeModel(models.Model):
#     author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     description = models.CharField(max_length=200)
#     slug = models.SlugField(null=False, unique=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_live = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('feed_me_detail', kwargs={'slug': self.slug})

#     class Meta:
#         ordering = ['-updated_at']

# class RssFeedMeFeeds(Feed):
#     title = "Feed Me"
#     link = "/feedme/"
#     description = "Recent free tutorials on LearnDjango.com."

#     def items(self):
#         return FeedMeModel.objects.order_by("-updated_at")[:100]

#     def item_title(self, item):
#         return item.title

#     def item_description(self, item):
#         return truncatewords(item.content, 30)

#     def item_lastupdated(self, item):
#         return item.updated_at

@register_setting
class WagtailSettings(BaseGenericSetting):
    site_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    homepage_link = models.URLField(
        null=True,
        blank=True,
    );
    footer1 = RichTextField(blank=True, null=True)
    footer2 = RichTextField(blank=True, null=True)
    panels = [
        FieldPanel('site_logo'),
        FieldPanel('homepage_link'),
        FieldPanel('footer1'),
        FieldPanel('footer2'),
    ]
    class Meta:
        verbose_name = "Default Settings for All Websites"

@register_setting
class WebsiteSettings(BaseSiteSetting):
    site_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    homepage_link = models.URLField(
        null=True,
        blank=True,
    );
    footer1 = RichTextField(blank=True, null=True)
    footer2 = RichTextField(blank=True, null=True)
    panels = [
        FieldPanel('site_logo'),
        FieldPanel('homepage_link'),
        FieldPanel('footer1'),
        FieldPanel('footer2'),
    ]
    class Meta:
        verbose_name = "Settings Per Website"

def notanytest(val):
    return (any([
        val is None,
        val == '',
        val == '<p></p>',
    ]))

class FaitMaPage(Page):
    body = RichTextField(blank=True, null=True)
    posts_index = StreamField([
        ('ghost_index_blog',GhostIndexBlock(required=False))
        ], use_json_field=True, blank=True, null=True
        , max_num=1)
    footer1 = RichTextField(blank=True, null=True)
    footer2 = RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('posts_index'),
        FieldPanel('footer1'),
        FieldPanel('footer2'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['website_settings'] = WebsiteSettings.for_request(request=request)
        context['wagtail_settings'] = WagtailSettings.load(request_or_site=request)
        for item in ['site_logo','homepage_link','footer1','footer2']:
            # print(item)
            context[item] = getattr(context['website_settings'],item)
            # print(context[item])
            if (notanytest(context[item])):
                context[item] = getattr(context['wagtail_settings'],item)
            elif (notanytest(context[item]) and hasattr(self,item)):
                context[item] = getattr(self,item)
            # print(context[item])
        return context

class FaitMaHomePageBlog(FaitMaPage):
    pass
    # ghost_filter = models.CharField(blank=True, null=True, max_length=32)
    # ghost_order = models.CharField(blank=True, null=True, max_length=32)
    # # ghost_formats = models.CharField(blank=True, null=True, max_length=32)
    # ghost_limit = models.CharField(blank=True, null=True, max_length=8)
    # ghost_include = models.CharField(blank=True, null=True, max_length=32)

    # content_panels = FaitMaPage.content_panels + [
    #     FieldPanel('ghost_filter'),
    #     FieldPanel('ghost_order'),
    #     FieldPanel('ghost_limit'),
    #     FieldPanel('ghost_include'),
    # ]

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     params = {'ghost_limit':request.GET.get('limit', self.ghost_limit) or 15, 'ghost_include':request.GET.get('include', self.ghost_include) or 'tags,authors','ghost_order':request.GET.get('order',self.ghost_order),'ghost_filter':request.GET.get('filter',self.ghost_filter),'ghost_page':request.GET.get('page', 1) }
    #     context['posts'] = lesgv.services.get_blog_posts(params)
    #     return context