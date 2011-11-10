
url="http://www.bbcgoodfood.com/content/local/seasonal/table/all/"

import urllib
import urllib2
from datetime import *
from BeautifulSoup import BeautifulSoup
import re

f = urllib.urlopen(url)
html = f.read()

soup = BeautifulSoup(''.join(html))

dataTable = soup.find('table',summary="Seasonal availability")


rows = dataTable.findAll('tr')
from recipemonkeyapp.models import GroceryItem
for item in rows:
	
	item_tag=item.find('th',scope="row")
	
	if item_tag is not None:
		try:
			name=item_tag.a.text
		except:
			name=item_tag.string.strip()

		print name
		
		g=GroceryItem.objects.filter(name__icontains=name)

		
		
		imgs=item.findAll('img')
		
		seasons=[]
		x=0
		startIdx=-1
		endIdx=-1
		for i in imgs:
			
			if ('best' in i['alt']):
						
				if startIdx==-1:
					endIdx=x
				elif endIdx>=startIdx or endIdx==-1:
					endIdx=x
				
			
			if 'coming' in i['alt']:
				startIdx=x+1
				
				if startIdx>=len(imgs):
					startIdx=0
			x+=1
		
		
		if startIdx!=-1 and endIdx!=-1:
			start=datetime.strptime(imgs[startIdx].parent['headers'].split()[1],'%b')
			end=datetime.strptime(imgs[endIdx].parent['headers'].split()[1],'%b')
		
			for gi in g:
				gi.seasonStart=start
				gi.seasonEnd=end
				gi.save()
	
		
	