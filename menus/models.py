
from django.db import models
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,

)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet




# Create your models here.
"""
Menus Models
"""
class MenuItem(Orderable):

    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=50

    )
    link_url = models.CharField(
        max_length=500,
        blank=True
        
    )
    
    link_page = models.ForeignKey(
        "wagtailcore.Page", 
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,

    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey("Menu", related_name="menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),

    ]


@register_snippet

class Menu(ClusterableModel):
    """ The main menu clusterable model
    """
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title",editable= True)
    
    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        
        ], heading="Menu"),
        InlinePanel("menu_items", label="Menu Item")

    ]

    def ___str___(self):
     return self.title