from django.db import models


from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.snippets.models import register_snippet

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify
from urllib.parse import urlparse, parse_qs, urlencode, parse_qsl


# Create your models here.

## Page que mostrará el index de las películas
## Hereda solo de Home y no descendientes

## Modelo para películas

