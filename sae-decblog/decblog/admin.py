#!/usr/bin/python
#-*- enconding:utf8 -*-

from django.contrib import admin

from .models import Post, Tag, Category

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)