# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import TestCase

from .models import (
    Section, Article, PrePopulatedPost, Color, Fabric, Book, Promo, Chapter, ChapterXtra1,
    Employee, Person, WorkHour, AdminOrderedCallable, Post, Language, Actor, Podcast, UndeletableObject,
    ComplexSortedPerson, UnchangeableObject
)
from django.db import connection
from django.db.transaction import atomic, set_rollback


class AdminViewBasicTest(TestCase):

    def test_1(self):
        c = connection.cursor()

        c.execute('INSERT INTO "admin_views_section" ("id") VALUES (NULL)')
        c.execute('INSERT INTO "admin_views_article" ("section_id", "another_section_id", "sub_section_id") VALUES (1, NULL, NULL)')
        c.execute('INSERT INTO "admin_views_book" ("id") VALUES (NULL)')
        c.execute('INSERT INTO "admin_views_chapter" ("book_id") VALUES (1)')
        c.execute('INSERT INTO "admin_views_prepopulatedpost" ("slug") VALUES (1)')
        c.execute('INSERT INTO "admin_views_color" ("id") VALUES (NULL)')
        c.execute('INSERT INTO "admin_views_fabric" ("id") VALUES (NULL)')
        c.execute('INSERT INTO "admin_views_promo" ("book_id") VALUES (1)')
        c.execute('INSERT INTO "admin_views_chapterxtra1" ("chap_id") VALUES (1)')
        c.execute('INSERT INTO "auth_user" ("password", "last_login", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined") VALUES (1, NULL, 0, 1, 1, 1, 1, 0, 1, 1)')
        c.execute('INSERT INTO "django_session" ("session_key", "session_data", "expire_date") SELECT 1, 1, 1')
        c.execute('INSERT INTO "django_admin_log" ("action_time", "user_id", "content_type_id", "object_id", "object_repr", "action_flag", "change_message") VALUES (1, 1, 21, 1, 1, 2, 1)')
        c.execute('INSERT INTO "admin_views_person" ("id") VALUES (NULL)')
        c.execute('INSERT INTO "admin_views_language" ("iso") VALUES (1)')
        c.execute('INSERT INTO "admin_views_media" ("name") VALUES (1)')
        c.execute('INSERT INTO "admin_views_podcast" ("media_ptr_id") SELECT 1')
        c.execute('INSERT INTO "admin_views_complexsortedperson" ("id") VALUES (NULL)')
        c.execute('INSERT INTO "admin_views_employee" ("id") VALUES (NULL)')
        c.execute('INSERT INTO "admin_views_workhour" ("employee_id") VALUES (1)')
        c.execute('INSERT INTO "admin_views_post" ("id") VALUES (NULL)')
        c.execute('INSERT INTO "admin_views_actor" ("id") VALUES (NULL)')
        c.execute('INSERT INTO "admin_views_undeletableobject" ("id") VALUES (NULL)')
        c.execute('INSERT INTO "admin_views_unchangeableobject" ("id") VALUES (NULL)')

    def test_2(self):
        c = connection.cursor()
        c.execute('INSERT INTO "admin_views_adminorderedcallable" ("id") VALUES (NULL)')
