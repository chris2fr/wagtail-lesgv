from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class FaitMaPage(Page):
    body = RichTextField()
    footer1 = RichTextField(blank=True, null=True)
    footer2 = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('footer1'),
        FieldPanel('footer2'),
    ]
