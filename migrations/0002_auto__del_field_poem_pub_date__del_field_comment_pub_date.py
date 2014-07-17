# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Poem.pub_date'
        db.delete_column(u'poems_poem', 'pub_date')

        # Deleting field 'Comment.pub_date'
        db.delete_column(u'poems_comment', 'pub_date')


    def backwards(self, orm):
        # Adding field 'Poem.pub_date'
        db.add_column(u'poems_poem', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, blank=True),
                      keep_default=False)

        # Adding field 'Comment.pub_date'
        db.add_column(u'poems_comment', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, blank=True),
                      keep_default=False)


    models = {
        u'poems.comment': {
            'Meta': {'object_name': 'Comment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'poem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poems.Poem']", 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'poems.poem': {
            'Meta': {'object_name': 'Poem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
