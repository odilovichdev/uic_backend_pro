from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(_("name"), max_length=250)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        db_table = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
