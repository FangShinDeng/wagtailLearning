from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page, models.Model):

    template = "home/index.html"
    banner_title = models.CharField(max_length=100, blank=False, null = True)
    banner_subtitle = RichTextField(features = ["bold", "ilatic"], default="subtitle")
    banner_image = models.ForeignKey(
        "wagtailimages.Image", 
        null = True,
        blank = False,
        on_delete = models.SET_NULL,
        related_name = "+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null = True,
        blank = False, 
        on_delete = models.SET_NULL,
        related_name = "+"
    )

    # max_count = 1 # 只能有一頁, 不能創建子頁
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta")
    ]

    class Meta:
        verbose_name = "OH Hello World" 
        verbose_name_plural = "PLURAL NAME"