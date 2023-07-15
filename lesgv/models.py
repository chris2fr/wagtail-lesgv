from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField #, StreamField
from wagtail.admin.panels import  FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)
import lesgv.services
# from lesgv.blocks import GhostIndexBlock
from modelcluster.fields import ParentalKey

from django import template
register = template.Library()

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
    )
    footer1 = RichTextField(blank=True, null=True)
    footer2 = RichTextField(blank=True, null=True)
    theme = models.CharField(max_length=32,choices=[('generique','generique'),('boule','boule'),('lesartsvoisins','lesartsvoisins'),],blank=True,null=True,default='generique')
    panels = [
        FieldPanel('site_logo'),
        FieldPanel('homepage_link'),
        FieldPanel('footer1'),
        FieldPanel('footer2'),
        FieldPanel('theme'),
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
    )
    footer1 = RichTextField(blank=True, null=True)
    footer2 = RichTextField(blank=True, null=True)
    theme = models.CharField(max_length=32,choices=[('generique','generique'),('boule','boule'),('lesartsvoisins','lesartsvoisins'),],blank=True,null=True,default='generique')
    csscolors = models.TextField(blank=True, null=True)
    panels = WagtailSettings.panels + [
        FieldPanel('csscolors'),
    ]
    
    class Meta:
        verbose_name = "Settings Per Website"

def notanytest(val):
    return (any([
        val is None,
        val == '',
        val == '<p></p>',
    ]))

class FaireMainPage(Page):
    body = RichTextField(blank=True, null=True)
    # posts_index = StreamField([
    #     ('ghost_index_blog',GhostIndexBlock(required=False))
    #     ], use_json_field=True, blank=True, null=True
    #     , max_num=1)
    footer1 = RichTextField(blank=True, null=True)
    footer2 = RichTextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    page_description = "Faire Ma Page, Une page"
    parent_page_types = ['wagtailcore.Page','lesgv.FaireMainHomePage','lesgv.FaireMainPage']
    subpage_types = ['lesgv.FaireMainPage','lesgv.FaireMainAgendaItemPage']
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        # FieldPanel('posts_index'),
        FieldPanel('image')
    ]
    settings_panels = [
        FieldPanel('footer1'),
        FieldPanel('footer2'),
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['website_settings'] = WebsiteSettings.for_request(request=request)
        context['wagtail_settings'] = WagtailSettings.load(request_or_site=request)

        for item in ['site_logo','homepage_link','footer1','footer2','theme']:
            context[item] = getattr(context['website_settings'],item)
            if (notanytest(context[item])):
                context[item] = getattr(context['wagtail_settings'],item)
            elif (notanytest(context[item]) and hasattr(self,item)):
                context[item] = getattr(self,item)
        context['menuitems'] = self.get_children().filter(live=True, show_in_menus=True)
        context['breadcrumbs'] = []
        for a in self.get_ancestors():
            if (not a.is_root()):
                breadcrumb = {
                    "url": a.url,
                    "title":a.title,
                    "children":[]
                }
                for c in a.get_children().filter(live=True, show_in_menus=True):
                    breadcrumb["children"] += [{
                        "url": c.url,
                        "title":c.title
                    }]
                context['breadcrumbs'] += [breadcrumb]
        if (not context['theme']):
            context['theme'] = "generique"
        context['static_images'] = {}
        for item in ['TL','TR','BL','BR','ML','MR','BC']:
            context['static_images'][item] = "images/fairemain/{theme}/fairemain_{item}.svg".format(theme = context['theme'],item = item)
        return context

class RelatedAgendaItemHomePage(Orderable):
    home_page = ParentalKey(
        'FaireMainHomePage',
        related_name='agenda_home',
    )
    agenda_item = models.ForeignKey(
        'FaireMainAgendaItemPage',
        related_name="agenda_item",
        on_delete=models.CASCADE,
    )
    panels = [
        FieldPanel('agenda_item'),
    ]

class FaireMainAgendaItemPage(FaireMainPage):
    url = models.URLField(blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    place = models.CharField(blank=True, null=True, max_length=128)
    place_url = models.URLField(blank=True, null=True)
    page_description = "Faire Ma Agenda Item Page, Un évènement"
    parent_page_types = ['lesgv.FaireMainPage','lesgv.FaireMainAgendaItemPage']
    subpage_types = ['lesgv.FaireMainAgendaItemPage']
    content_panels = FaireMainPage.content_panels + [
        FieldPanel('url'),
        FieldPanel('start'),
        FieldPanel('end'),
        FieldPanel('place'),
        FieldPanel('place_url'),
    ] 

class FaireMainHomePage(FaireMainPage):
    agenda = RichTextField(blank=True, null=True)
    ghost_tag = models.CharField(blank=True, null=True, max_length=32)
    ghost_filter = models.CharField(blank=True, null=True, max_length=32)
    ghost_order = models.CharField(blank=True, null=True, max_length=32)
    # ghost_formats = models.CharField(blank=True, null=True, max_length=32)
    ghost_limit = models.CharField(blank=True, null=True, max_length=8)
    ghost_include = models.CharField(blank=True, null=True, max_length=32)
    page_description = "Faire Main Home Page: Une page home "
    parent_page_types =['wagtailcore.Page']
    subpage_types = ['lesgv.FaireMainPage','lesgv.FaireMainAgendaItemPage']
    content_panels = [
        InlinePanel('agenda_home',label="Items de l'agenda"),
    ]  + FaireMainPage.content_panels + [
        FieldPanel('agenda'),
        FieldPanel('ghost_tag'),
        FieldPanel('ghost_filter'),
        FieldPanel('ghost_order'),
        FieldPanel('ghost_limit'),
        FieldPanel('ghost_include'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        params = {
            'ghost_tag': self.ghost_tag,
            'ghost_limit': self.ghost_limit,
            'ghost_include': self.ghost_include,
            'ghost_order': self.ghost_order,
            'ghost_filter': self.ghost_filter,
            'ghost_page':  request.GET.get('page', 1)
        }
        context['posts'] = lesgv.services.get_blog_posts(lesgv.services.ProcessGhostParams(params))
        context['related_agenda'] = RelatedAgendaItemHomePage.objects.filter(home_page=self)
        return context 