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
	paginator = Paginator(article_list, 50) # Show 30 contacts per page
	
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
		
		context_dict ={'loc': "browse",
		'output_doc':art,
		'found':True
		}
		
	except Article.DoesNotExist:
		 return HttpResponseRedirect("/home/")
		
	return render(request,'home/news_page.html',context=context_dict)    

def browse(request):
	display_list=["STBT",'STIMES','FT','WSJO','GRDN','WP']
	display_pic={\
	"STBT":"/images/STBT_square.png",\
	"STIMES":"/images/ST_square.jpg",\
	"FT":"/images/FT_square.jpg",\
	"WSJO":"/images/WSJO_square.jpg",\
	"GRDN":"/images/GRDN_square.jpg",\
	#"WP":"/images/WP_square.jpg",\
	}
	art={}
	entries_no={}
	
	package=[]
	total_entries_no = Article.objects.count()
	
	for item in display_list:
		try:
			art=Article.objects.filter(ARTICLE_ID__startswith=item)
			#print (item)
			newsite=art[0].NEWSITE
			entries_no= art.count()
			latest=art.latest('DATE').DATE.date()
			#print([{'art':art,'entries_no':entries_no,'display_pic':display_pic[item]}])
			package.append({'item':item,'entries_no':entries_no,'display_pic':display_pic[item],\
			'newsite':newsite,'latest':latest\
			})
		except Article.DoesNotExist: 
			pass
		except Exception as e:
			print (e)
		
	context_dict ={'loc': "browse",
	'art':art,
	'entries_no':entries_no,
	'display_pic':display_pic,
	'package':package,
	'total_entries_no':total_entries_no,
	}	
	return render(request,'home/browse.html',context=context_dict)    

def browseSite(request,newsite):
	try:
		article_list=Article.objects.filter(ARTICLE_ID__startswith=newsite).order_by('-DATE','HEADLINE')
		newsite=article_list[0].NEWSITE
		for item in article_list:
			item.DATE=item.DATE.date()
		entries_no= article_list.count()
			
		paginator = Paginator(article_list, 15) # Show 30 contacts per page
		
		page = request.GET.get('page',1)
		
		try:
			articles = paginator.page(page)
		except PageNotAnInteger:
			articles = paginator.page(1)
		except EmptyPage:
			articles = paginator.page(paginator.num_pages)
		
		
		context_dict ={'loc': "browse",
		'articles':articles,
		'newsite':newsite,
		'entries_no':entries_no,
		'found':True
		}
		
	except Article.DoesNotExist:
		 return HttpResponseRedirect("/home/browse")
		
	return render(request,'home/browsesite.html',context=context_dict) 	