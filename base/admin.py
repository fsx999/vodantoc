# coding=utf-8
from __future__ import unicode_literals
from djangocms_text_ckeditor.widgets import TextEditorWidget
from django.db import models
from django.contrib import admin
from base.models import Professeur, PaysModel, RegroupementSalle
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


admin.site.register(RegroupementSalle)
admin.site.register(Professeur)
admin.site.register(PaysModel)
admin.site.register(Salle, SalleAdmin)
