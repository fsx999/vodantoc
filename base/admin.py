# coding=utf-8
from __future__ import unicode_literals
from djangocms_text_ckeditor.widgets import TextEditorWidget
from django.db import models
from django.contrib import admin
from base.models import Professeur, PaysModel, RegroupementSalle, Eleve, Inscription, Annee, TypePaiement, ClassPaiement, \
    Paiement
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
    list_filter = ('inscription__annee',)
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

class PaiementInline(admin.TabularInline):
    model = Paiement

class InscriptionAdmin(admin.ModelAdmin):
    search_fields = ('eleve__nom', 'eleve__prenom')
    inlines = (PaiementInline,)
    list_filter = ('annee', )

    def get_queryset(self, request):
        annee_en_cour = Annee.objects.get(annee_en_cousr=True)
        return super(InscriptionAdmin, self).get_queryset(request).filter(annee=annee_en_cour)


admin.site.register(RegroupementSalle)
admin.site.register(Professeur)
admin.site.register(PaysModel)
admin.site.register(Annee)
admin.site.register(Salle, SalleAdmin)
admin.site.register(Eleve, EleveAdmin)
admin.site.register(TypePaiement)
admin.site.register(ClassPaiement)
admin.site.register(Inscription, InscriptionAdmin)