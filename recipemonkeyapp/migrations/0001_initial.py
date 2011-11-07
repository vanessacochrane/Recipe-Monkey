# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Instruction'
        db.create_table('recipemonkeyapp_instruction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('step', self.gf('django.db.models.fields.TextField')()),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.Recipe'])),
        ))
        db.send_create_signal('recipemonkeyapp', ['Instruction'])

        # Adding model 'Recipe'
        db.create_table('recipemonkeyapp_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('cuisine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.Cuisine'], null=True, blank=True)),
            ('course', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('serving', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('servingMeasure', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.Source'], null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('recipemonkeyapp', ['Recipe'])

        # Adding M2M table for field instructions on 'Recipe'
        db.create_table('recipemonkeyapp_recipe_instructions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['recipemonkeyapp.recipe'], null=False)),
            ('instruction', models.ForeignKey(orm['recipemonkeyapp.instruction'], null=False))
        ))
        db.create_unique('recipemonkeyapp_recipe_instructions', ['recipe_id', 'instruction_id'])

        # Adding model 'Cuisine'
        db.create_table('recipemonkeyapp_cuisine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['recipemonkeyapp.Cuisine'])),
        ))
        db.send_create_signal('recipemonkeyapp', ['Cuisine'])

        # Adding model 'Source'
        db.create_table('recipemonkeyapp_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('recipemonkeyapp', ['Source'])

        # Adding model 'StorageLog'
        db.create_table('recipemonkeyapp_storagelog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('storage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.Storage'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
            ('dateAdded', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('dateChanged', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2011, 11, 7, 3, 51, 3, 309958))),
        ))
        db.send_create_signal('recipemonkeyapp', ['StorageLog'])

        # Adding model 'StorageItem'
        db.create_table('recipemonkeyapp_storageitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('storage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.Storage'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
            ('quantityMeasure', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('recipemonkeyapp', ['StorageItem'])

        # Adding model 'GroceryItem'
        db.create_table('recipemonkeyapp_groceryitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.GroceryCategory'])),
            ('seasonStart', self.gf('django.db.models.fields.DateField')(null=True)),
            ('seasonEnd', self.gf('django.db.models.fields.DateField')(null=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.Store'], null=True)),
            ('unitcost', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('unitweight', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('recipemonkeyapp', ['GroceryItem'])

        # Adding model 'GroceryCategory'
        db.create_table('recipemonkeyapp_grocerycategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='child', null=True, to=orm['recipemonkeyapp.GroceryCategory'])),
        ))
        db.send_create_signal('recipemonkeyapp', ['GroceryCategory'])

        # Adding model 'RecipeIngredient'
        db.create_table('recipemonkeyapp_recipeingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quantity', self.gf('django.db.models.fields.FloatField')()),
            ('quantityMeasure', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('processing', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('keyIngredientFlag', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.GroceryItem'])),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.Recipe'])),
        ))
        db.send_create_signal('recipemonkeyapp', ['RecipeIngredient'])

        # Adding model 'Store'
        db.create_table('recipemonkeyapp_store', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('storeType', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('recipemonkeyapp', ['Store'])

        # Adding model 'Storage'
        db.create_table('recipemonkeyapp_storage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('recipemonkeyapp', ['Storage'])

        # Adding model 'UserFoodPrefs'
        db.create_table('recipemonkeyapp_userfoodprefs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('recipemonkeyapp', ['UserFoodPrefs'])

        # Adding M2M table for field likes on 'UserFoodPrefs'
        db.create_table('recipemonkeyapp_userfoodprefs_likes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userfoodprefs', models.ForeignKey(orm['recipemonkeyapp.userfoodprefs'], null=False)),
            ('groceryitem', models.ForeignKey(orm['recipemonkeyapp.groceryitem'], null=False))
        ))
        db.create_unique('recipemonkeyapp_userfoodprefs_likes', ['userfoodprefs_id', 'groceryitem_id'])

        # Adding M2M table for field dislikes on 'UserFoodPrefs'
        db.create_table('recipemonkeyapp_userfoodprefs_dislikes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userfoodprefs', models.ForeignKey(orm['recipemonkeyapp.userfoodprefs'], null=False)),
            ('groceryitem', models.ForeignKey(orm['recipemonkeyapp.groceryitem'], null=False))
        ))
        db.create_unique('recipemonkeyapp_userfoodprefs_dislikes', ['userfoodprefs_id', 'groceryitem_id'])

        # Adding model 'Planner'
        db.create_table('recipemonkeyapp_planner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('recipemonkeyapp', ['Planner'])

        # Adding M2M table for field users on 'Planner'
        db.create_table('recipemonkeyapp_planner_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('planner', models.ForeignKey(orm['recipemonkeyapp.planner'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('recipemonkeyapp_planner_users', ['planner_id', 'user_id'])

        # Adding M2M table for field recipes on 'Planner'
        db.create_table('recipemonkeyapp_planner_recipes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('planner', models.ForeignKey(orm['recipemonkeyapp.planner'], null=False)),
            ('recipe', models.ForeignKey(orm['recipemonkeyapp.recipe'], null=False))
        ))
        db.create_unique('recipemonkeyapp_planner_recipes', ['planner_id', 'recipe_id'])


    def backwards(self, orm):
        
        # Deleting model 'Instruction'
        db.delete_table('recipemonkeyapp_instruction')

        # Deleting model 'Recipe'
        db.delete_table('recipemonkeyapp_recipe')

        # Removing M2M table for field instructions on 'Recipe'
        db.delete_table('recipemonkeyapp_recipe_instructions')

        # Deleting model 'Cuisine'
        db.delete_table('recipemonkeyapp_cuisine')

        # Deleting model 'Source'
        db.delete_table('recipemonkeyapp_source')

        # Deleting model 'StorageLog'
        db.delete_table('recipemonkeyapp_storagelog')

        # Deleting model 'StorageItem'
        db.delete_table('recipemonkeyapp_storageitem')

        # Deleting model 'GroceryItem'
        db.delete_table('recipemonkeyapp_groceryitem')

        # Deleting model 'GroceryCategory'
        db.delete_table('recipemonkeyapp_grocerycategory')

        # Deleting model 'RecipeIngredient'
        db.delete_table('recipemonkeyapp_recipeingredient')

        # Deleting model 'Store'
        db.delete_table('recipemonkeyapp_store')

        # Deleting model 'Storage'
        db.delete_table('recipemonkeyapp_storage')

        # Deleting model 'UserFoodPrefs'
        db.delete_table('recipemonkeyapp_userfoodprefs')

        # Removing M2M table for field likes on 'UserFoodPrefs'
        db.delete_table('recipemonkeyapp_userfoodprefs_likes')

        # Removing M2M table for field dislikes on 'UserFoodPrefs'
        db.delete_table('recipemonkeyapp_userfoodprefs_dislikes')

        # Deleting model 'Planner'
        db.delete_table('recipemonkeyapp_planner')

        # Removing M2M table for field users on 'Planner'
        db.delete_table('recipemonkeyapp_planner_users')

        # Removing M2M table for field recipes on 'Planner'
        db.delete_table('recipemonkeyapp_planner_recipes')


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
            'Meta': {'object_name': 'GroceryItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.GroceryCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'seasonEnd': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'seasonStart': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Store']", 'null': 'True'}),
            'unitcost': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'unitweight': ('django.db.models.fields.FloatField', [], {'default': '0'})
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
            'recipes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipemonkeyapp.Recipe']", 'symmetrical': 'False'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'})
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
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Source']", 'null': 'True', 'blank': 'True'})
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
            'date': ('django.db.models.fields.DateField', [], {}),
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
            'dateChanged': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2011, 11, 7, 3, 51, 3, 333216)'}),
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
        'recipemonkeyapp.userfoodprefs': {
            'Meta': {'object_name': 'UserFoodPrefs'},
            'dislikes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'food_dislikes'", 'null': 'True', 'to': "orm['recipemonkeyapp.GroceryItem']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'food_likes'", 'null': 'True', 'to': "orm['recipemonkeyapp.GroceryItem']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['recipemonkeyapp']
