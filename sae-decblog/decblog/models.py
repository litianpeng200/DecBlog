#!/usr/bin/python
# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify
from django.core.urlresolvers import reverse

import markdown2


@python_2_unicode_compatible
class Post(models.Model):
	title = models.CharField(max_length=256,default='New Post')
	slug = models.CharField(max_length=256,blank=True,null=True,default='new-post')
	author = models.ForeignKey(User)
	pub_date = models.DateTimeField(auto_now_add = True)
	abstract = models.TextField(null = True, blank = True)
	content_raw = models.TextField()
	content_html = models.TextField(null = True, blank = True)
	tags = models.ManyToManyField('Tag',blank=True)
	category = models.ForeignKey('Category',blank=True,null=True)
	is_draft = models.BooleanField(default=False)

	def save(self,*args,**kwargs):
		self.content_html = markdown2.markdown(self.content_raw, extras=['code-friendly', 'fenced-code-blocks']).encode('utf-8')
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("post",kwargs={'slug':self.slug})

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(max_length=256)
	slug = models.CharField(max_length=256,blank=True,null=True,default='uname')

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super(Tag,self).save(*args,**kwargs)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length=256)
	slug = models.CharField(max_length=256,default='uname')

	def save(self,*args,**kwargs):
		self.slug = slugify(self.name)
		super(Category,self).save(*args,**kwargs)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class BlogSetting(models.Model):
	name = models.CharField(max_length=255)
	value = models.CharField(max_length=255)

	def __str__(self):
		return self.name