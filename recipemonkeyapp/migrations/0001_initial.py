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
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('step', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipemonkeyapp.Recipe'])),
        ))
        db.send_create_signal('recipemonkeyapp', ['Instruction'])

        # Adding model 'Recipe'
        db.create_table('recipemonkeyapp_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2048)),
        ))
        db.send_create_signal('recipemonkeyapp', ['Recipe'])


    def backwards(self, orm):
        
        # Deleting model 'Instruction'
        db.delete_table('recipemonkeyapp_instruction')

        # Deleting model 'Recipe'
        db.delete_table('recipemonkeyapp_recipe')


    models = {
        'recipemonkeyapp.instruction': {
            'Meta': {'object_name': 'Instruction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipemonkeyapp.Recipe']"}),
            'step': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        'recipemonkeyapp.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        }
    }

    complete_apps = ['recipemonkeyapp']
