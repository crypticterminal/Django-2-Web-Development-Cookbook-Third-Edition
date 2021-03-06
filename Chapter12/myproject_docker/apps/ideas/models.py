from django.urls import reverse, NoReverseMatch
from django.db import models
from django.utils.translation import ugettext_lazy as _
from treebeard.mp_tree import MP_Node

from utils.models import CreationModificationDateMixin, UrlMixin
from utils.fields import (MultilingualCharField,
                          MultilingualTextField)


class Category(MP_Node, CreationModificationDateMixin):
    class Meta:
        verbose_name = _("Idea Category")
        verbose_name_plural = _("Idea Categories")

    title = MultilingualCharField(_("Title"), max_length=200)

    def __str__(self):
        return self.title


class Idea(UrlMixin):
    class Meta:
        verbose_name = _("Idea")
        verbose_name_plural = _("Ideas")

    title = MultilingualCharField(_("Title"), max_length=200)
    subtitle = MultilingualCharField(_("Subtitle"),
                                     max_length=200,
                                     blank=True)
    description = MultilingualTextField(_("Description"),
                                        blank=True)
    is_original = models.BooleanField(_("Original"))
    categories = models.ManyToManyField(Category,
                                        blank=True,
                                        related_name="ideas",
                                        verbose_name=_(
                                            "Categories"))

    def __str__(self):
        return self.title

    def get_url_path(self):
        try:
            return reverse("idea_detail", kwargs={"id": self.pk})
        except NoReverseMatch:
            return ""
