# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DjangoBBModel'
        db.create_table(u'base_djangobbmodel', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('nb_last_post', self.gf('django.db.models.fields.IntegerField')(default=5)),
        ))
        db.send_create_signal(u'base', ['DjangoBBModel'])

        # Adding model 'EntryZiniaCmsPlugins'
        db.create_table(u'base_entryziniacmsplugins', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('nb_last_post', self.gf('django.db.models.fields.IntegerField')(default=3)),
        ))
        db.send_create_signal(u'base', ['EntryZiniaCmsPlugins'])

        # Adding model 'Professeur'
        db.create_table(u'base_professeur', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date_naissance', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'base', ['Professeur'])

        # Adding model 'PaysModel'
        db.create_table(u'base_paysmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'base', ['PaysModel'])

        # Adding model 'RegroupementSalle'
        db.create_table(u'base_regroupementsalle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=60, null=True)),
            ('pays', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.PaysModel'], null=True)),
        ))
        db.send_create_signal(u'base', ['RegroupementSalle'])

        # Adding model 'ListeProfesseur'
        db.create_table(u'base_listeprofesseur', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'base', ['ListeProfesseur'])

        # Adding model 'ListeSalle'
        db.create_table(u'base_listesalle', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('pays', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.PaysModel'])),
        ))
        db.send_create_signal(u'base', ['ListeSalle'])

        # Adding model 'Salle'
        db.create_table(u'base_salle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('horaire', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('adresse', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_creation', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('pays', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.PaysModel'])),
            ('secteur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.RegroupementSalle'], null=True)),
        ))
        db.send_create_signal(u'base', ['Salle'])

        # Adding M2M table for field professeurs on 'Salle'
        m2m_table_name = db.shorten_name(u'base_salle_professeurs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('salle', models.ForeignKey(orm[u'base.salle'], null=False)),
            ('professeur', models.ForeignKey(orm[u'base.professeur'], null=False))
        ))
        db.create_unique(m2m_table_name, ['salle_id', 'professeur_id'])


    def backwards(self, orm):
        # Deleting model 'DjangoBBModel'
        db.delete_table(u'base_djangobbmodel')

        # Deleting model 'EntryZiniaCmsPlugins'
        db.delete_table(u'base_entryziniacmsplugins')

        # Deleting model 'Professeur'
        db.delete_table(u'base_professeur')

        # Deleting model 'PaysModel'
        db.delete_table(u'base_paysmodel')

        # Deleting model 'RegroupementSalle'
        db.delete_table(u'base_regroupementsalle')

        # Deleting model 'ListeProfesseur'
        db.delete_table(u'base_listeprofesseur')

        # Deleting model 'ListeSalle'
        db.delete_table(u'base_listesalle')

        # Deleting model 'Salle'
        db.delete_table(u'base_salle')

        # Removing M2M table for field professeurs on 'Salle'
        db.delete_table(db.shorten_name(u'base_salle_professeurs'))


    models = {
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
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'horaire': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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