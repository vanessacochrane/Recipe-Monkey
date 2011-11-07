# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'StorageItem.date'
        db.add_column('recipemonkeyapp_storageitem', 'date', self.gf('django.db.models.fields.DateField')(null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'StorageItem.date'
        db.delete_column('recipemonkeyapp_storageitem', 'date')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Recipe']"}),
            'step': ('django.db.models.fields.TextField', [], {})
        },
        'recipemonkeyapp.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'cuisine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Cuisine']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipemonkeyapp.GroceryItem']", 'through': "orm['recipemonkeyapp.RecipeIngredient']", 'symmetrical': 'False'}),
            'instructions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'steps'", 'symmetrical': 'False', 'to': "orm['recipemonkeyapp.Instruction']"}),
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
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'quantityMeasure': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Recipe']"})
        },
        'recipemonkeyapp.source': {
            'Meta': {'object_name': 'Source'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'recipemonkeyapp.storage': {
            'Meta': {'object_name': 'Storage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'recipemonkeyapp.storageitem': {
            'Meta': {'object_name': 'StorageItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'storage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Storage']"})
        },
        'recipemonkeyapp.store': {
            'Meta': {'object_name': 'Store'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'storeType': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['recipemonkeyapp']
