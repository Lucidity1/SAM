from lxml import etree as ET
import re
import pandas as pd
import operator
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SAM.settings')
list=os.listdir("articles/")
TO_DIR="scanned_articles/"

COL=["DOCTYPE",'AN','HEADLINE','CATEGORY','AUTHOR','NEWSITE','DATE','WORDCOUNT','FOLDER','LEADPARA','TAILPARAS']
data=pd.DataFrame(columns=COL)
db_list=[]

import sqlite3
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
conn = sqlite3.connect(os.path.join(BASE_DIR, 'SAM/db.sqlite3'))

import django
django.setup()
from home.models import Article

from django.utils.html import escape

#from home.models import ArticleRaw

#def add_line(ARTICLE_ID,CONTENT):
#	c=ArticleRaw.objects.get_or_create(ARTICLE_ID=ARTICLE_ID,CONTENT=CONTENT)[0]
#	c.save()
	
def parseArticle(item):
	global data
	global COL
	global db_list
	#text=''
	#with open("articles/"+item) as f:
	#	for line in f:
	#		text+=line
			
	
	tree=ET.parse("articles/"+item)
	root=tree.getroot()
	archivedoc=root.find('ArchiveDoc')
	replyitem=root.find('ReplyItem')
	selectdata=root.find('SelectData')

	meta=['doctype','an']
	temp=[]

	for item in meta:
		content=root.get(item)
		temp.append(content)
		if item=='an':
			an=content

	try:
		for item in archivedoc.iter('Headline'):
			head=item.find("Para").text
	except Exception as e:
		head=""
	temp.append(head.strip())

	try:
		for item in archivedoc.iter('SectionName'):
			cat=item.text
	except Exception as e:
		cat=""
	temp.append(cat)

	try:
		for item in archivedoc.iter('Byline'):
			author=item.text
	except Exception as e:
		author=""
	temp.append(author)

	temp.append(replyitem.find("SrcName").text)
	temp.append(replyitem.find("Date").get("value"))
	temp.append(replyitem.find("Num").get("value"))

	temp.append(selectdata.find("FolderName").text)

	leadpara=""
	try:
		for item in archivedoc.iter('LeadPara'):
			for item in item.findall("Para"):
				leadpara+=item.text
				leadpara+="\n\n"
		
	except Exception as e:
		pass
	temp.append(leadpara)#.strip())

	tailparas=""
	try:
		for item in archivedoc.iter('TailParas'):
			for item in item.findall("Para"): 
				tailparas+=item.text
				for item in item.findall("ELink"):
					tailparas+=' '
					tailparas+=item.text
				tailparas+="\n\n"
		
	except Exception as e:
		pass
	temp.append(tailparas)

	#print (temp)
	#print (an)
	if an not in db_list:
		df2= pd.DataFrame([temp], columns=COL)
		data=data.append(df2,ignore_index=True)
	else:
		print (an+" already in DB") 
    
    
WORD_COL=["DOCTYPE",'AN','HEADLINE','CATEGORY','AUTHOR','NEWSITE','FOLDER','LEADPARA','TAILPARAS']

def parseAll(list):
	global data
	global COL
	global db_list
	data=pd.DataFrame(columns=COL)

	#Check what is already inside
	#db_list = [item for item in Article.objects.values_list('ARTICLE_ID')]
	db_list= Article.objects.all().values_list('ARTICLE_ID', flat=True) 
	#print (db_list)

	for item in list:
		try:
			parseArticle(item)
		except Exception as e:
			print ("Unable to parse",item)
			print (e)
	data['DATE'] = pd.to_datetime(data['DATE'], format="%Y%m%d").dt.tz_localize('Asia/Singapore')

	#for item in WORD_COL:
	#    try:
	#        data[item]=(data[item].str.encode('ascii','ignore'))
	#    except Exception as e:
	#        print (e)
	#        print (item)

			
if __name__=='__main__':

	print("Starting articles population script..")
	parseAll(list)
	
	#if os.path.exists(os.path.join(BASE_DIR, 'SAM/my_db')):
	#	print ("DB exist.")
	#print (data.head)
	
	'''
	from django.conf import settings
	from sqlalchemy import create_engine
	
	database_name = settings.DATABASES['default']['NAME']
	print (database_name)
	database_url = 'sqlite:///{}'.format(database_name)



	engine = create_engine(database_url, echo=False)
	#print (Article.__name__)
	data["id"] = data.index
	data.to_sql('home_article', con=engine, if_exists='replace')
	
	
	#Article.objects.bulk_create( for vals in data.to_dict())

	from sqlalchemy.engine.reflection import Inspector
	inspector = Inspector.from_engine(engine)
	for table_name in inspector.get_table_names():
		print (table_name)
		
	'''

	
	df_records = data.to_dict('records')

	#WARNING NO SANITIZATION
	model_instances = [Article(\
	DOCTYPE=(record['DOCTYPE']),\
	ARTICLE_ID=(record['AN']),\
	WORDCOUNT=record['WORDCOUNT'],\
	DATE=record['DATE'],\
	HEADLINE=(record['HEADLINE']),\
	CATEGORY=(record['CATEGORY']),\
	AUTHOR=(record['AUTHOR']),\
	NEWSITE=(record['NEWSITE']),\
	LEADPARA=(record['LEADPARA']),\
	TAILPARAS=(record['TAILPARAS']),\
	) for record in df_records]
	
	#print ("PRINTING")
	#print (model_instances)
	
	try: 
		print ("Commiting to DB")
		Article.objects.bulk_create(model_instances)
		print (str(len(model_instances))+" committed")
		
		for item in list:
			try:
				os.rename(os.path.join("articles",item), os.path.join(TO_DIR,item))
			except Exception as e:
				print ("Unable to move",item)
				print (e)
			
	except Exception as e:
		print ("Unable to commit")
		print (e)
