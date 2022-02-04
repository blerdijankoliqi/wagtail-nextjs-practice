from pyexpat import features
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    #only use templte. Homepage model.
    templates = "home/home_page.html"

    #homepage BANNER section.
    banner_title = models.CharField(max_length=100, blank=False, default="Hey")
    banner_subtitle = models.CharField(max_length=100, blank=False, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    #homepage ABOUT section.
    section_about_title = models.CharField(max_length=100, blank=False, null=True)
    section_about_subtitle = models.CharField(max_length=200, blank=False, null=True)
    banner_tekst = RichTextField(null=True)
    section_about_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    #homepage APARTMENTS section.
    section_apartments_title = models.CharField(max_length=100, blank=False, null=True)
    section_apartments_subtitle = models.CharField(max_length=200, blank=False, null=True)
    #homepage SERVICES section.
    section_services_title = models.CharField(max_length=100, blank=False, null=True)
    section_services_subtitle = models.CharField(max_length=200, blank=False, null=True)
    #homepage SPECIAL OFFERS section.
    section_special_offers_title = models.CharField(max_length=100, blank=False, null=True)
    section_special_offers_subtitle = models.CharField(max_length=200, blank=False, null=True)
    #homepage TESTIMONIALS section.
    section_testimonial_title = models.CharField(max_length=100, blank=False, null=True)
    section_testimonial_subtitle = models.CharField(max_length=200, blank=False, null=True)
    #homepage NEWSLETTER section.
    section_newsletter_title = models.CharField(max_length=100, blank=False, null=True)
    section_newsletter_subtitle = models.CharField(max_length=200, blank=False, null=True)


    #now we need to add this field to the Dashboard. We do that with content panel. 
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        FieldPanel("section_about_title"),
        FieldPanel("section_about_subtitle"),
        FieldPanel("banner_tekst"),
        ImageChooserPanel("section_about_image"),
        FieldPanel("section_apartments_title"),
        FieldPanel("section_apartments_subtitle"),
        FieldPanel("section_services_title"),
        FieldPanel("section_services_subtitle"),
        FieldPanel("section_special_offers_title"),
        FieldPanel("section_special_offers_subtitle"),
        FieldPanel("section_testimonial_title"),
        FieldPanel("section_testimonial_subtitle"),
        FieldPanel("section_newsletter_title"),
        FieldPanel("section_newsletter_subtitle")
    ]