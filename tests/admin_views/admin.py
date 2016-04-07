# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    Article, Section
)



class ArticleInline(admin.TabularInline):
    model = Article
    fk_name = 'section'
    fieldsets = (
        ('Some other fields', {
            'fields': ('section',)
        }),
    )


site = admin.AdminSite(name="admin")
site.register(Section, save_as=True, inlines=[ArticleInline], readonly_fields=['name_property'])
