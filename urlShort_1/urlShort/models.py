from django.db import models
class UrlData(models.Model):
    url = models.URLField()
    slug = models.SlugField(unique=True)