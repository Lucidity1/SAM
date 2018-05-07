from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):

	DOCTYPE=models.CharField(max_length=128)
	ARTICLE_ID=models.CharField(max_length=128, unique=True)
	WORDCOUNT=models.IntegerField(null=True)
	DATE=models.DateTimeField()
	HEADLINE=models.CharField(max_length=128)
	CATEGORY=models.CharField(max_length=128,null=True)
	AUTHOR=models.CharField(max_length=128,null=True)
	NEWSITE=models.CharField(max_length=128,null=True)
	FOLDER=models.CharField(max_length=128,null=True)
	
	LEADPARA=models.CharField(max_length=128,null=True)
	TAILPARAS=models.CharField(max_length=128,null=True)

	class Meta:
		verbose_name_plural = 'Articles'
	
	def __str__(self):
		return self.ARTICLE_ID
		
	def __unicode__(self):
		return self.ARTICLE_ID

'''
class ArticleRaw(models.Model):

	ARTICLE_ID=models.CharField(max_length=128, unique=True)
	CONTENT=models.CharField(max_length=128)


	class Meta:
		verbose_name_plural = 'ArticleRaws'
	
	def __str__(self):
		return self.ARTICLE_ID
		
	def __unicode__(self):
		return self.ARTICLE_ID
'''