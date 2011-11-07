# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Store'
        db.create_table('recipemonkeyapp_store', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('storeType', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('recipemonkeyapp', ['Store'])

        # Adding model 'RecipeIngredient'
        db.create_table('recipemonkeyapp_recipeingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('quantityMeasure', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('processing', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('keyIngredientFlag', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.GroceryItem'])),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.Recipe'])),
        ))
        db.send_create_signal('recipemonkeyapp', ['RecipeIngredient'])

        # Adding model 'Cuisine'
        db.create_table('recipemonkeyapp_cuisine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['recipemonkeyapp.Cuisine'])),
        ))
        db.send_create_signal('recipemonkeyapp', ['Cuisine'])

        # Adding model 'GroceryItem'
        db.create_table('recipemonkeyapp_groceryitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.GroceryCategory'])),
            ('seasonStart', self.gf('django.db.models.fields.DateField')()),
            ('seasonEnd', self.gf('django.db.models.fields.DateField')()),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.Store'])),
        ))
        db.send_create_signal('recipemonkeyapp', ['GroceryItem'])

        # Adding model 'GroceryCategory'
        db.create_table('recipemonkeyapp_grocerycategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['recipemonkeyapp.GroceryCategory'])),
        ))
        db.send_create_signal('recipemonkeyapp', ['GroceryCategory'])

        # Adding model 'Source'
        db.create_table('recipemonkeyapp_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('recipemonkeyapp', ['Source'])

        # Adding field 'Recipe.cuisine'
        db.add_column('recipemonkeyapp_recipe', 'cuisine', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['recipemonkeyapp.Cuisine']), keep_default=False)

        # Adding field 'Recipe.course'
        db.add_column('recipemonkeyapp_recipe', 'course', self.gf('django.db.models.fields.CharField')(default='Main', max_length=256), keep_default=False)

        # Adding field 'Recipe.serving'
        db.add_column('recipemonkeyapp_recipe', 'serving', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'Recipe.servingMeasure'
        db.add_column('recipemonkeyapp_recipe', 'servingMeasure', self.gf('django.db.models.fields.CharField')(default='People', max_length=256), keep_default=False)

        # Adding field 'Recipe.source'
        db.add_column('recipemonkeyapp_recipe', 'source', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['recipemonkeyapp.Source']), keep_default=False)

        # Adding field 'Recipe.note'
        db.add_column('recipemonkeyapp_recipe', 'note', self.gf('django.db.models.fields.CharField')(default='', max_length=2048), keep_default=False)

        # Changing field 'Recipe.name'
        db.alter_column('recipemonkeyapp_recipe', 'name', self.gf('django.db.models.fields.CharField')(max_length=256))


    def backwards(self, orm):
        
        # Deleting model 'Store'
        db.delete_table('recipemonkeyapp_store')

        # Deleting model 'RecipeIngredient'
        db.delete_table('recipemonkeyapp_recipeingredient')

        # Deleting model 'Cuisine'
        db.delete_table('recipemonkeyapp_cuisine')

        # Deleting model 'GroceryItem'
        db.delete_table('recipemonkeyapp_groceryitem')

        # Deleting model 'GroceryCategory'
        db.delete_table('recipemonkeyapp_grocerycategory')

        # Deleting model 'Source'
        db.delete_table('recipemonkeyapp_source')

        # Deleting field 'Recipe.cuisine'
        db.delete_column('recipemonkeyapp_recipe', 'cuisine_id')

        # Deleting field 'Recipe.course'
        db.delete_column('recipemonkeyapp_recipe', 'course')

        # Deleting field 'Recipe.serving'
        db.delete_column('recipemonkeyapp_recipe', 'serving')

        # Deleting field 'Recipe.servingMeasure'
        db.delete_column('recipemonkeyapp_recipe', 'servingMeasure')

        # Deleting field 'Recipe.source'
        db.delete_column('recipemonkeyapp_recipe', 'source_id')

        # Deleting field 'Recipe.note'
        db.delete_column('recipemonkeyapp_recipe', 'note')

        # Changing field 'Recipe.name'
        db.alter_column('recipemonkeyapp_recipe', 'name', self.gf('django.db.models.fields.CharField')(max_length=2048))


    models = {
        'recipemonkeyapp.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['recipemonkeyapp.Cuisine']"})
        },
        'recipemonkeyapp.grocerycategory': {
            'Meta': {'object_name': 'GroceryCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['recipemonkeyapp.GroceryCategory']"})
        },
        'recipemonkeyapp.groceryitem': {
            'Meta': {'object_name': 'GroceryItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.GroceryCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'seasonEnd': ('django.db.models.fields.DateField', [], {}),
            'seasonStart': ('django.db.models.fields.DateField', [], {}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Store']"})
        },
        'recipemonkeyapp.instruction': {
            'Meta': {'object_name': 'Instruction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Recipe']"}),
            'step': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        'recipemonkeyapp.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'cuisine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Cuisine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'serving': ('django.db.models.fields.IntegerField', [], {}),
            'servingMeasure': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Source']"})
        },
        'recipemonkeyapp.recipeingredient': {
            'Meta': {'object_name': 'RecipeIngredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.GroceryItem']"}),
            'keyIngredientFlag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'processing': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'quantityMeasure': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Recipe']"})
        },
        'recipemonkeyapp.source': {
            'Meta': {'object_name': 'Source'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'recipemonkeyapp.store': {
            'Meta': {'object_name': 'Store'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'storeType': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['recipemonkeyapp']
