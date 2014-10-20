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
    inlines = [InscriptionInline]

    search_fields = ('nom', 'prenom')

admin.site.register(RegroupementSalle)
admin.site.register(Professeur)
admin.site.register(PaysModel)
admin.site.register(Annee)
admin.site.register(Salle, SalleAdmin)
admin.site.register(Eleve, EleveAdmin)