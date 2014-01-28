# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'gifsong.sfwness'
        db.add_column(u'gifsong_gifsong', 'sfwness',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=3),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'gifsong.sfwness'
        db.delete_column(u'gifsong_gifsong', 'sfwness')


    models = {
        u'gifsong.gifsong': {
            'Meta': {'object_name': 'gifsong'},
            'audio_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sfwness': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3'})
        }
    }

    complete_apps = ['gifsong']