from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import  FieldPanel, MultiFieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)

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
    panels = [
        FieldPanel('site_logo'),
        FieldPanel('homepage_link'),
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
    panels = [
        FieldPanel('site_logo'),
        FieldPanel('homepage_link'),
    ]
    class Meta:
        verbose_name = "Settings Per Website"

class FaitMaPage(Page):
    body = RichTextField()
    footer1 = RichTextField(blank=True, null=True)
    footer2 = RichTextField(blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('footer1'),
        FieldPanel('footer2'),
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['website_settings'] = WebsiteSettings.for_request(request=request)
        context['wagtail_settings'] = WagtailSettings.load(request_or_site=request)
        for item in ['site_logo','homepage_link']:
            print(item)
            context[item] = getattr(context['website_settings'],item)
            print(context[item])
            if ((not context[item]) or context[item] is None):
                context[item] = getattr(context['wagtail_settings'],item)
            print(context[item])
            
                
        return context
