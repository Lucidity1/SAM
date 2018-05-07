from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import numpy as np
from dateutil import tz
import datetime as dt
import calendar
from django.http import HttpResponseRedirect

from home.models import Article#, ArticleRaw 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import lxml.html
from lxml import etree
	
@login_required()
def index(request):
	entries_no = Article.objects.count()
	article_list=Article.objects.all()
	paginator = Paginator(article_list, 30) # Show 30 contacts per page
	
	page = request.GET.get('page',1)
	
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	
	context_dict ={'loc': "index",
	'entries_no':entries_no,
	'articles':articles,
	}
	return render(request,'home/index.html',context=context_dict)

@login_required()
def empty_page(request):
	context_dict ={}
	return render(request,'home/empty_page.html',context=context_dict)


@login_required()
def news_page(request,article_id):

	try:
		art=Article.objects.get(ARTICLE_ID=article_id)
		art.DATE=art.DATE.date()
		
		context_dict ={'loc': "index",
		'output_doc':art,
		'found':True
		}
		
	except Article.DoesNotExist:
		 return HttpResponseRedirect("/home/")
		
	return render(request,'home/news_page.html',context=context_dict)    
