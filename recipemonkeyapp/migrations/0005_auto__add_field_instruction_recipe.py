# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Instruction.recipe'
        db.add_column('recipemonkeyapp_instruction', 'recipe', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['recipemonkeyapp.Recipe']), keep_default=False)

        # Removing M2M table for field instructions on 'Recipe'
        db.delete_table('recipemonkeyapp_recipe_instructions')


    def backwards(self, orm):
        
        # Deleting field 'Instruction.recipe'
        db.delete_column('recipemonkeyapp_instruction', 'recipe_id')

        # Adding M2M table for field instructions on 'Recipe'
        db.create_table('recipemonkeyapp_recipe_instructions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['recipemonkeyapp.recipe'], null=False)),
            ('instruction', models.ForeignKey(orm['recipemonkeyapp.instruction'], null=False))
        ))
        db.create_unique('recipemonkeyapp_recipe_instructions', ['recipe_id', 'instruction_id'])


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
            'step': ('django.db.models.fields.TextField', [], {})
        },
        'recipemonkeyapp.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'cuisine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Cuisine']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipemonkeyapp.GroceryItem']", 'through': "orm['recipemonkeyapp.RecipeIngredient']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
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
