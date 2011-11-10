"""
Class to call the Tesco API for product information

http://www.techfortesco.com/forum/index.php?PHPSESSID=m0qo482jfkdt3u12eg0n25urv0&

"""

import urllib
import json
import csv


class Tesco:
	
	app_key="0438E4B51C378DAA6525"
	developer_key="5JHcix7BJC7TwiC2NxCv"
	base_url="https://secure.techfortesco.com/groceryapi_b1/restservice.aspx?command="
	session_key=""
	user="cochrane.davey@gmail.com"
	password="Lucy1720"
	products=[]
	categories=[]
	
	def __init__(self,session_key=None):
		
		if session_key is None:
			self.SetSessionKey()
		else:
			self.session_key=session_key
	
	def CreateProductsCSV(self):
		
		fields=['Id', 'Name', 'EANBarcode', 'UnitPrice','UnitType','Category','Price','BaseProductId']
		
		self.CreateCSV(self.products,fields,'inventory/sql/tesco-products.csv')

	def CreateCategoriesCSV(self):
		
		fields=['Id', 'Name', 'Parent', 'Type']
		
		self.CreateCSV(self.categories,fields,'inventory/sql/tesco-categories.csv')

	def CreateCSV(self,data,fields,csvfile):
		
		
		myfile = open(csvfile, 'w')
		
		w = csv.DictWriter(myfile,fields ,dialect='excel',quoting=csv.QUOTE_NONNUMERIC)
		w.writerow(dict(zip(fields, fields)))
		for d in data:
			w.writerow(d)
			
			
		myfile.close()

	def CreateUrl(self,command,args):
		
		if command=='LOGIN':
			url=self.base_url + command  \
				+ "&EMAIL=" + self.user + "&PASSWORD=" + self.password \
				+ "&developerkey=" + self.developer_key \
				+ "&applicationkey=" + self.app_key
		else:
			url=self.base_url + command  + args\
				+ "&SESSIONKEY=" + self.session_key 
			
		return url

	def SetSessionKey(self):
		
		url = self.CreateUrl('LOGIN','')

		print "Logging in to Tesco...."
		data=json.loads(urllib.urlopen(url).read())
				
		self.session_key=data['SessionKey']
		print "..session Key: " + self.session_key

	def GetCategories(self):

		print 'Getting catgeories'
		url=self.CreateUrl('LISTPRODUCTCATEGORIES','')
		# print url
		data=json.loads(urllib.urlopen(url).read())

		for d in data['Departments']:
			
			deptid=d['Id']
			name=d['Name']
			parent=''
			cattype='Department'
			
			self.categories.append({'Name':name,'Id':deptid,'Parent':parent,'Type':cattype})
			for a in d['Aisles']:
				aid=a['Id']
				name=a['Name']
				cattype='Aisle'
				
				self.categories.append({'Name':name,'Id':aid,'Parent':deptid,'Type':cattype})
				
				for s in a['Shelves']:
					catid=s['Id']
					name=s['Name']
					cattype='Shelf'
					self.categories.append({'Name':name,'Id':catid,'Parent':aid,'Type':cattype})
	
	
	def PrintCategories(self):
		
		print self.categories				

	def GetAllProducts(self):
		
		for c in self.categories:
			if c['Type']=='Shelf':
				self.GetProductsInCategory(c['Id'])
				
		

	def GetProductBySearch(self,id):

		url=self.CreateUrl("PRODUCTSEARCH","&SEARCHTEXT=%s&EXTENDEDINFO=%s" % (str(id),'N'))
		# print url

		print 'Getting products by id ' + str(id)
		data=json.loads(urllib.urlopen(url).read())

		if data['TotalProductCount']==0:
			return []
			
		#print data
		products=[]
		for p in data['Products']:
			props=['Name','EANBarcode','UnitPrice','UnitType','Price','BaseProductId']
			myp={}
			for key,val in p.iteritems():
				for prop in props:
					if prop==key:
						myp[key]=val

			#myp['Category']=cat	
			products.append(myp)
		return products

	def GetProductsInCategory(self,cat):
		
		url=self.CreateUrl('LISTPRODUCTSBYCATEGORY','&CATEGORY=' + str(cat))
		# print url
		
		print 'Getting products in cat ' + str(cat)
		data=json.loads(urllib.urlopen(url).read())
		
		for p in data['Products']:
			props=['Name','EANBarcode','UnitPrice','UnitType','Price','BaseProductId']
			myp={}
			for key,val in p.iteritems():
				for prop in props:
					if prop==key:
						myp[key]=val
			
			myp['Category']=cat	
			self.products.append(myp)
			
	def ProcessProducts(self):
		
		print 'Processing products..'
		for p in self.products:
			
			p['Weight']=p['Price']/p['UnitPrice']
			
			if p['UnitType'] == 'kg':
				print 'skip'
				# p['Name']=p['Name'].replace(" %dG" % (1000*p['Weight']),'')
	
	def PrintProducts(self):
		print self.products
			


def tesco_download():
	
	from recipemonkeyapp.models import GroceryItem,GroceryItemInfo
	from datetime import datetime
	#groceries where tescoid is defined
	groceries=GroceryItem.objects.exclude(tescoid='')
	
	#create a Tesco object
	t=Tesco()
	
	dt=datetime.today().date()
	#load tesco data for each item
	for g in groceries:
		data=t.GetProductBySearch(g.tescoid)
	
		if data==[]:
			print 'No data found for %s' % g.name
			continue
			
			
		data=data[0]
		try:
			gi=g.groceryiteminfo_set.get(date=dt)
			print "...updating existing record"
		except:
			gi=GroceryItemInfo()
			
		gi.date=dt
		gi.item=g
		gi.unitPrice=data['UnitPrice']
		gi.price=data['Price']
		gi.unitType=data['UnitType']
		gi.source='Tesco'
		gi.save()
		
		if g.EANBarcode != data['EANBarcode']:	
			g.EANBarcode=data['EANBarcode']
			g.save()
	
		if g.tescoName != data['Name']:	
			g.tescoName=data['Name']
			g.save()
		
	
def tesco_assignids():

	from recipemonkeyapp.models import GroceryItem
	from datetime import datetime
	#groceries where tescoid is defined
	groceries=GroceryItem.objects.filter(tescoid='')

	#create a Tesco object
	t=Tesco()

	dt=datetime.today().date()
	#load tesco data for each item

	for g in groceries:
	
		
		srch=g.name
		while True:
			tesco_products=t.GetProductBySearch(srch)
			for i in range(0,len(tesco_products)):
			
				p=tesco_products[i]
			
				print "[%d] %s" % (i,p['Name']) 
			
			print "n: new search, s: skip, [0....i]: use product i, x: exit"
			choice = raw_input("Enter choice: ")
		
			if choice=='x':
				return
		
			elif choice=='s':
				break
				
			elif choice=='n':
				
				srch = raw_input("Enter new search term: ")
				
			elif int(choice)>=0 and int(choice) <= len(tesco_products):
				g.tescoid=tesco_products[int(choice)]['BaseProductId']
				g.save()
				break
		
			
		
