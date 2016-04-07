# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse

from .models import (
    Section, Article, PrePopulatedPost, Color, Fabric, Book, Promo, Chapter, ChapterXtra1,
    Employee, Person, WorkHour, AdminOrderedCallable, Post, Language, Actor, Podcast, UndeletableObject,
    ComplexSortedPerson, UnchangeableObject
)


@override_settings(ROOT_URLCONF='admin_views.urls')
class AdminViewBasicTest(TestCase):

    def test_basic_edit_POST(self):
        s1 = Section.objects.create()
        a1 = Article.objects.create(section=s1)


        b1 = Book.objects.create()
        chap1 = Chapter.objects.create(book=b1)
        PrePopulatedPost.objects.create()
        Color.objects.create()
        Fabric.objects.create()
        Promo.objects.create(book=b1)
        ChapterXtra1.objects.create(chap=chap1)

        url = reverse('admin:admin_views_section_change', args=(s1.pk,))
        superuser = User.objects.create_superuser(username='super', password='s', email='s@e')
        self.client.force_login(superuser)
        inline_post_data = {
            "name": "Test section",
            # inline data
            "article_set-TOTAL_FORMS": "1",
            "article_set-INITIAL_FORMS": "1",
            "article_set-MAX_NUM_FORMS": "0",
            "article_set-0-id": a1.pk,
            "article_set-0-section": s1.pk,
        }
        self.client.post(url, inline_post_data)
        Person.objects.create()
        Language.objects.create(iso='ar')
        Podcast.objects.create()
        ComplexSortedPerson.objects.create()

    def test_sort_indicators_admin_order(self):
        AdminOrderedCallable.objects.create()

    def test_popup_dismiss_related(self):
        e1 = Employee.objects.create()
        WorkHour.objects.create(employee=e1)
        Post.objects.create()
        Actor.objects.create()
        UndeletableObject.objects.create()
        UnchangeableObject.objects.create()
