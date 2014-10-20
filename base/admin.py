# coding=utf-8
from __future__ import unicode_literals
from djangocms_text_ckeditor.widgets import TextEditorWidget
from django.db import models
from django.contrib import admin
from base.models import Professeur, PaysModel, RegroupementSalle, Eleve, Inscription, Annee
from base.models import Salle
from django import forms


class form(forms.ModelForm):
    class Meta:
        widgets = {
            'adresse': TextEditorWidget
        }


class SalleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TextEditorWidget},
    }
    # form = form

class InscriptionInline(admin.TabularInline):
    model = Inscription

class EleveAdmin(admin.ModelAdmin):
    list_filter = ('annee',)
    inlines = [InscriptionInline]
    list_editable = ('phone', 'email', 'adresse')
    list_display = ('nom', 'prenom', 'adresse', 'phone', 'email', 'inscriptions')
    readonly_fields = ('inscriptions',)
    search_fields = ('nom', 'prenom')
    ordering = ('nom', )

    def inscriptions(self, obj):
        reponse = ""
        for x in obj.inscription.all().order_by('annee'):
            reponse += "{} {}<br>".format(x.annee.annee, x.salle)
        return reponse
    inscriptions.allow_tags = True

admin.site.register(RegroupementSalle)
admin.site.register(Professeur)
admin.site.register(PaysModel)
admin.site.register(Annee)
admin.site.register(Salle, SalleAdmin)
admin.site.register(Eleve, EleveAdmin)