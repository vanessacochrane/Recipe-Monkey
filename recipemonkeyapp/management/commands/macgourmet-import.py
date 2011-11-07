from django.core.management.base import BaseCommand, CommandError
from recipemonkeyapp.models import *
import sqlite3
from datetime import *


def convert_fractions(str):

	str=str.strip()

	if str=='1/2':
		return 0.5
	
	if str=='1 1/2':
		return 1.5
		
	if str=='1/4' or str=='1/8-1/4':
		return 0.25
	
	if str=='':
		return 0
	
	if str=='3/4':
		return 7.25
	
	return float(str)
	
	
class Command(BaseCommand):
	args = '<macgourment sqllite3 file>'
	help = 'Reads a macgourmet sqlfile and imports its data into the app'

	def handle(self, *args, **options):
			
		if len(args) < 1:
			raise CommandError('Requires arguments %s' % self.args)

		db=args[0]

		self.stdout.write('Reading sqlite file %s\n' % (db))
		
		try:
			conn = sqlite3.connect(db)
		except:
			raise CommandError('db connection failed: %s' % db)	
		
		conn.row_factory = sqlite3.Row
		self.stdout.write('.Quering db\n')
		
		c = conn.cursor()
		
		sql="""
		select 
			r.recipe_id as rID,
			r.name as rName,
			r.source as rSource,
			r.servings as servings,
			r.course_id as rCourse
		
		from recipe as r
		
		"""
		
		c.execute(sql)
		
		self.stdout.write('.Creating recipes\n')
		for r in c:
		
			try:
				rec=Recipe.objects.get(pk=r['rId'])
			except:
				rec=Recipe()
			
			rec.id=r['rId']
			rec.name=r['rName']
			rec.serving=r['servings']
			
			
			try:
				src=Source.objects.get(name=r['rSource'])
			except:
				src=Source()
				
			src.name=r['rSource']
			src.save()
		
		
			rec.source=src
		
			rec.save()
			c2 = conn.cursor()
			sql="""
			select 
				i.ingredient_id as iID,
				i.description as iName,
				i.direction as processing,
				i.quantity as quantity,
				i.measurement as quantityMeasure
			
			from ingredient as i
			where description<>'' and recipe_id='%s'

			""" % (r['rId'])

			c2.execute(sql)
			
			for r2 in c2:
				iName=r2['iName'].strip()
				try:
					ing=GroceryItem.objects.get(name=iName)
				except:
					ing=GroceryItem()
					self.stdout.write('..adding grocery item %s\n' % (r2['iName']))
					
				ing.name=iName
				ing.category_id=11 #default to 'other'
			
				ing.save()
				
				try:
					ri=RecipeIngredient.objects.get(item=r2['iId'],recipe=r['rId'])
				except:
					ri=RecipeIngredient()
				
				ri.item_id=ing.id
				ri.recipe_id=r['rId']
				ri.quantity=convert_fractions(r2['quantity'])
				ri.quantityMeasure=r2['quantityMeasure']
				ri.processing=r2['processing']
				ri.save()
				
				
			sql="""
			select 
				d.direction_id as dID,
				d.sort_order as sort_order,
				d.directions_text as step
	
			from direction as d
			where recipe_id='%s'
			

			""" % (r['rId'])

			c2.execute(sql)

			for r2 in c2:	
				try:
					inst=Instruction.objects.get(recipe=r['rId'])
				except:
					inst=Instruction()
				
				inst.id=r2['dId']
				inst.recipe_id=r['rId']
				inst.order=r2['sort_order']
				inst.step=r2['step']
				inst.save()
				
			
			sql="""
			select 
				n.recipe_note_id as nID,
				n.note_text as note
			
			
			from recipe_note as n
			where recipe_id='%s'

			""" % (r['rId'])

			c2.execute(sql)	
			
			for r2 in c2:
				rec.note=r2['note']
				
			rec.save()
		
		c2.close()
		
		c.close()
		
		conn.close()