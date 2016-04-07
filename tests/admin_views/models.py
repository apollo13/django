# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Section(models.Model):
    pass

class Article(models.Model):
    section = models.ForeignKey(Section, models.CASCADE, null=True, blank=True)
    another_section = models.ForeignKey(Section, models.CASCADE, null=True, blank=True, related_name='+')
    sub_section = models.ForeignKey(Section, models.SET_NULL, null=True, blank=True, related_name='+')


class Book(models.Model):
    pass

class Promo(models.Model):
    book = models.ForeignKey(Book, models.CASCADE)

class Chapter(models.Model):
    book = models.ForeignKey(Book, models.CASCADE)

class ChapterXtra1(models.Model):
    chap = models.OneToOneField(Chapter, models.CASCADE, verbose_name='¿Chap?')

class Color(models.Model):
    pass

class Actor(models.Model):
    pass

class Fabric(models.Model):
    pass

class Person(models.Model):
    pass

class Media(models.Model):
    name = models.CharField(max_length=60)

class Podcast(Media):
    pass

class Language(models.Model):
    iso = models.CharField(max_length=5, primary_key=True)

class PrePopulatedPost(models.Model):
    slug = models.SlugField()

class Post(models.Model):
    pass

class Employee(models.Model):
    pass

class WorkHour(models.Model):
    employee = models.ForeignKey(Employee, models.CASCADE)

class ComplexSortedPerson(models.Model):
    pass

class AdminOrderedCallable(models.Model):
    pass

class UndeletableObject(models.Model):
    pass

class UnchangeableObject(models.Model):
    pass
