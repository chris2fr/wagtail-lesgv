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
