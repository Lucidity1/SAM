# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from home.models import Article
#from home.models import ArticleRaw

admin.site.register(Article)
#admin.site.register(ArticleRaw)