'''FLEX PAGE MODEL.PY'''
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

# Create your models here.

class About(Page):

    template = "about/about.html"
    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

        