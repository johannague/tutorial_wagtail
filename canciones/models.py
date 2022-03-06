"""  CANCIONES MODELS"""

from turtle import position
from django.db import models
from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.snippets.models import register_snippet

# Create your models here.

## Page que mostrará el index de las Canciones
## Hereda solo de Home y no descendientes

## Modelo para Canciones


class Cancion(models.Model):
    title = models.CharField('título', max_length=250)
    #slug = models.SlugField()
    position = models.IntegerField()
    rating = models.DecimalField(max_digits=6, decimal_places=4)
    link = models.URLField()
    place = models.IntegerField()
    imagen = models.URLField()


    panels = [
        FieldPanel('title'),
        FieldPanel('position'),
        FieldPanel('rating'),
        FieldPanel('link'),
        FieldPanel('place'),
        FieldPanel('imagen'),
        
    ]
    def __str__(self):
        return f'{self.title} ({self.position})'

class CancionesIndexPage(Page):
    introduccion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduccion', classname="full")
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        context['canciones'] = Cancion.objects.all()
        
        return context



    