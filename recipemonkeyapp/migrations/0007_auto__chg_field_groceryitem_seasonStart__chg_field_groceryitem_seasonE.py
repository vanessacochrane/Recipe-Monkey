# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'GroceryItem.seasonStart'
        db.alter_column('recipemonkeyapp_groceryitem', 'seasonStart', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'GroceryItem.seasonEnd'
        db.alter_column('recipemonkeyapp_groceryitem', 'seasonEnd', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'GroceryItem.store'
        db.alter_column('recipemonkeyapp_groceryitem', 'store_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.Store'], null=True))


    def backwards(self, orm):
        
        # Changing field 'GroceryItem.seasonStart'
        db.alter_column('recipemonkeyapp_groceryitem', 'seasonStart', self.gf('django.db.models.fields.DateField')(default=1))

        # Changing field 'GroceryItem.seasonEnd'
        db.alter_column('recipemonkeyapp_groceryitem', 'seasonEnd', self.gf('django.db.models.fields.DateField')(default=1))

        # Changing field 'GroceryItem.store'
        db.alter_column('recipemonkeyapp_groceryitem', 'store_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['recipemonkeyapp.Store']))


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
            'seasonEnd': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'seasonStart': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Store']", 'null': 'True'})
        },
        'recipemonkeyapp.instruction': {
            'Meta': {'object_name': 'Instruction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Recipe']"}),
            'step': ('django.db.models.fields.TextField', [], {})
        },
        'recipemonkeyapp.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'cuisine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Cuisine']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipemonkeyapp.GroceryItem']", 'through': "orm['recipemonkeyapp.RecipeIngredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'serving': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'servingMeasure': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Source']", 'null': 'True'})
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
