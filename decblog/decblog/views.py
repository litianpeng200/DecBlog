#!/urs/bin/python
#-*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView

from .models import Post, Tag, Category, BlogSetting


class PostListView(ListView):
	model = Post
	paginate_by = 3

class PostDetailView(DetailView):
	pass