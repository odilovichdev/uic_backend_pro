from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .translation import *  # noqa
from .models import Category


@admin.register(Category)
class CategoryModelAdmin(TabbedTranslationAdmin, admin.ModelAdmin):
    list_display = "id", "name"
    list_filter = "name",
