from django.db import models
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    """
    A model representing a blog post with title, author, content, publish date, and optional slug.
    """

    title = models.CharField(_("title"), max_length=200, null=False, blank=False)
    author = models.CharField(_("author"), max_length=200, null=False, blank=False)
    content = models.TextField(_("content"), null=False, blank=False)
    publish_date = models.DateTimeField(_("publish_date"), null=False, blank=False)
    slug = models.SlugField(null=True, blank=True)
