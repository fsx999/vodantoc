# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Paiement'
        db.create_table(u'base_paiement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(default='C', to=orm['base.TypePaiement'], blank=True)),
            ('classe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.ClassPaiement'])),
            ('inscription', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Inscription'])),
            ('montant', self.gf('django.db.models.fields.FloatField')()),
            ('numero_cheque', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('banque', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
        ))
        db.send_create_signal(u'base', ['Paiement'])

        # Adding model 'ClassPaiement'
        db.create_table(u'base_classpaiement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'base', ['ClassPaiement'])

        # Adding model 'TypePaiement'
        db.create_table(u'base_typepaiement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'base', ['TypePaiement'])


    def backwards(self, orm):
        # Deleting model 'Paiement'
        db.delete_table(u'base_paiement')

        # Deleting model 'ClassPaiement'
        db.delete_table(u'base_classpaiement')

        # Deleting model 'TypePaiement'
        db.delete_table(u'base_typepaiement')


    models = {
        u'base.agendamodel': {
            'Meta': {'object_name': 'AgendaModel', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'nb_last_event': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        u'base.annee': {
            'Meta': {'object_name': 'Annee'},
            'annee': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'annee_en_cours': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'base.classpaiement': {
            'Meta': {'object_name': 'ClassPaiement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'base.eleve': {
            'Meta': {'object_name': 'Eleve'},
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'code_postal': ('django.db.models.fields.CharField', [], {'default': "'92130'", 'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'date_naissance': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ville': ('django.db.models.fields.CharField', [], {'default': "'issy les moulineaux'", 'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        u'base.entryziniacmsplugins': {
            'Meta': {'object_name': 'EntryZiniaCmsPlugins', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'nb_last_post': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        u'base.inscription': {
            'Meta': {'object_name': 'Inscription'},
            'annee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Annee']"}),
            'eleve': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'inscription'", 'to': u"orm['base.Eleve']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'principale': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'salle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Salle']"})
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
        u'base.paiement': {
            'Meta': {'object_name': 'Paiement'},
            'banque': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'classe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.ClassPaiement']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inscription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Inscription']"}),
            'montant': ('django.db.models.fields.FloatField', [], {}),
            'numero_cheque': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'default': "'C'", 'to': u"orm['base.TypePaiement']", 'blank': 'True'})
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        u'base.regroupementsalle': {
            'Meta': {'object_name': 'RegroupementSalle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'pays': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.PaysModel']", 'null': 'True'})
        },
        u'base.salle': {
            'Meta': {'object_name': 'Salle'},
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
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
            'secteur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.RegroupementSalle']", 'null': 'True', 'blank': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        },
        u'base.typepaiement': {
            'Meta': {'object_name': 'TypePaiement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '3'})
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