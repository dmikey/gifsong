# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'gifsong'
        db.create_table(u'gifsong_gifsong', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('audio_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'gifsong', ['gifsong'])


    def backwards(self, orm):
        # Deleting model 'gifsong'
        db.delete_table(u'gifsong_gifsong')


    models = {
        u'gifsong.gifsong': {
            'Meta': {'object_name': 'gifsong'},
            'audio_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['gifsong']