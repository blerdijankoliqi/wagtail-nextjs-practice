from pyexpat import features
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    #only use templte. Homepage model.
    templates = "home/home_page.html"

    #this is a additional field for the homepage model.
    banner_title = models.CharField(max_length=100, blank=False, default="Hey")
    #this is the rich tekst editor.
    banner_tekst = RichTextField(null=True)
    # this is going to be the main image.
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    #now we need to add this field to the Dashboard. We do that with content panel. 
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_tekst"),
        ImageChooserPanel("banner_image")
    ]