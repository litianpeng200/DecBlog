#!/urs/bin/python
#-*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Post, Tag, Category, BlogSetting

class PostListView(ListView):
	model = Post
	paginate_by = 3

class PostListView_by_Tag(PostListView):
	def get_queryset(self):
		self.tag = get_object_or_404(Tag,name=self.args[0])
		return Post.objects.filter(tags=self.tag)

class PostListView_by_Category(PostListView):
	def get_queryset(self):
		self.category = get_object_or_404(Category,name=self.args[0])
		return Post.objects.filter(category=self.category)

class PostDetailView(DetailView):
	model = Post