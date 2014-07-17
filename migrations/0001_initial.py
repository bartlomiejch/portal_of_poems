# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poem'
        db.create_table(u'poems_poem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('like', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'poems', ['Poem'])

        # Adding model 'Comment'
        db.create_table(u'poems_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('nick', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('poem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poems.Poem'], null=True)),
        ))
        db.send_create_signal(u'poems', ['Comment'])

        # Adding model 'Stropha'
        db.create_table(u'poems_stropha', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stropha', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'poems', ['Stropha'])


    def backwards(self, orm):
        # Deleting model 'Poem'
        db.delete_table(u'poems_poem')

        # Deleting model 'Comment'
        db.delete_table(u'poems_comment')

        # Deleting model 'Stropha'
        db.delete_table(u'poems_stropha')


    models = {
        u'poems.comment': {
            'Meta': {'object_name': 'Comment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'poem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poems.Poem']", 'null': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'poems.poem': {
            'Meta': {'object_name': 'Poem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'poems.stropha': {
            'Meta': {'object_name': 'Stropha'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stropha': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['poems']
