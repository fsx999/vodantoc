# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Salle.computed_address'
        db.add_column(u'base_salle', 'computed_address',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Salle.latitude'
        db.add_column(u'base_salle', 'latitude',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Salle.longitude'
        db.add_column(u'base_salle', 'longitude',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Salle.geocode_error'
        db.add_column(u'base_salle', 'geocode_error',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Salle.computed_address'
        db.delete_column(u'base_salle', 'computed_address')

        # Deleting field 'Salle.latitude'
        db.delete_column(u'base_salle', 'latitude')

        # Deleting field 'Salle.longitude'
        db.delete_column(u'base_salle', 'longitude')

        # Deleting field 'Salle.geocode_error'
        db.delete_column(u'base_salle', 'geocode_error')


    models = {
        u'base.agendamodel': {
            'Meta': {'object_name': 'AgendaModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'nb_last_event': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        u'base.djangobbmodel': {
            'Meta': {'object_name': 'DjangoBBModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'nb_last_post': ('django.db.models.fields.IntegerField', [], {'default': '5'})
        },
        u'base.entryziniacmsplugins': {
            'Meta': {'object_name': 'EntryZiniaCmsPlugins', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'nb_last_post': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        u'base.listeprofesseur': {
            'Meta': {'object_name': 'ListeProfesseur', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'base.listesalle': {
            'Meta': {'object_name': 'ListeSalle', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.PaysModel']"})
        },
        u'base.paysmodel': {
            'Meta': {'object_name': 'PaysModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'base.professeur': {
            'Meta': {'object_name': 'Professeur'},
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_naissance': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'base.regroupementsalle': {
            'Meta': {'object_name': 'RegroupementSalle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.PaysModel']", 'null': 'True'})
        },
        u'base.salle': {
            'Meta': {'object_name': 'Salle'},
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'computed_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geocode_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'horaire': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.PaysModel']"}),
            'professeurs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['base.Professeur']", 'null': 'True', 'blank': 'True'}),
            'secteur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.RegroupementSalle']", 'null': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['base']