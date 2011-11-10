# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SubRecipe'
        db.create_table('recipemonkeyapp_subrecipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mainRecipe', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parent', to=orm['recipemonkeyapp.Recipe'])),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subrecipe', to=orm['recipemonkeyapp.Recipe'])),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
            ('optional', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('recipemonkeyapp', ['SubRecipe'])

        # Removing M2M table for field subrecipes on 'Recipe'
        db.delete_table('recipemonkeyapp_recipe_subrecipes')


    def backwards(self, orm):
        
        # Deleting model 'SubRecipe'
        db.delete_table('recipemonkeyapp_subrecipe')

        # Adding M2M table for field subrecipes on 'Recipe'
        db.create_table('recipemonkeyapp_recipe_subrecipes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_recipe', models.ForeignKey(orm['recipemonkeyapp.recipe'], null=False)),
            ('to_recipe', models.ForeignKey(orm['recipemonkeyapp.recipe'], null=False))
        ))
        db.create_unique('recipemonkeyapp_recipe_subrecipes', ['from_recipe_id', 'to_recipe_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
            'EANBarcode': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'GroceryItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.GroceryCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'seasonEnd': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'seasonStart': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'seasonal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Store']", 'null': 'True', 'blank': 'True'}),
            'tescoid': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'recipemonkeyapp.groceryiteminfo': {
            'Meta': {'object_name': 'GroceryItemInfo'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.GroceryItem']"}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'unitPrice': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'unitType': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'recipemonkeyapp.instruction': {
            'Meta': {'object_name': 'Instruction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Recipe']"}),
            'step': ('django.db.models.fields.TextField', [], {})
        },
        'recipemonkeyapp.planner': {
            'Meta': {'object_name': 'Planner'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipemonkeyapp.Recipe']", 'through': "orm['recipemonkeyapp.PlannerMeal']", 'symmetrical': 'False'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'})
        },
        'recipemonkeyapp.plannermeal': {
            'Meta': {'object_name': 'PlannerMeal'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'planner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Planner']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Recipe']"})
        },
        'recipemonkeyapp.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'course': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'cuisine': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Cuisine']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipemonkeyapp.GroceryItem']", 'through': "orm['recipemonkeyapp.RecipeIngredient']", 'symmetrical': 'False'}),
            'instructions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'steps'", 'symmetrical': 'False', 'to': "orm['recipemonkeyapp.Instruction']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'serving': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'servingMeasure': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Source']", 'null': 'True', 'blank': 'True'}),
            'subrecipes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'subRecipes'", 'to': "orm['recipemonkeyapp.Recipe']", 'through': "orm['recipemonkeyapp.SubRecipe']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        'recipemonkeyapp.recipeingredient': {
            'Meta': {'object_name': 'RecipeIngredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.GroceryItem']"}),
            'keyIngredientFlag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'processing': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'quantityMeasure': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
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
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'quantityMeasure': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'storage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Storage']"})
        },
        'recipemonkeyapp.storagelog': {
            'Meta': {'object_name': 'StorageLog'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'dateAdded': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dateChanged': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
        },
        'recipemonkeyapp.subrecipe': {
            'Meta': {'object_name': 'SubRecipe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mainRecipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent'", 'to': "orm['recipemonkeyapp.Recipe']"}),
            'optional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quantity': ('django.db.models.fields.FloatField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subrecipe'", 'to': "orm['recipemonkeyapp.Recipe']"})
        },
        'recipemonkeyapp.userfoodprefs': {
            'Meta': {'object_name': 'UserFoodPrefs'},
            'dislikes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'food_dislikes'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['recipemonkeyapp.GroceryItem']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'food_likes'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['recipemonkeyapp.GroceryItem']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['recipemonkeyapp']
