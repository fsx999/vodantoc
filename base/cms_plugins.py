# coding=utf-8
from calendarium.models import Event
from zinnia.models import Entry
from base.models import  EntryZiniaCmsPlugins, ListeSalle, Salle, AgendaModel
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
__author__ = 'paul'
import datetime




# class ArticleInternaltionalNational(CMSPluginBase):
#     model = EntryZiniaCmsPlugins
#     name = u"Actualités internationales et nationales"
#     render_template = "base/actualite_inter_national.html"
#
#     def render(self, context, instance, placeholder):
#         posts_internationals = Entry.objects.filter(categories__slug="actualite-internationale").order_by('-last_update')[:instance.nb_last_post]
#         posts_nationals = Entry.objects.filter(categories__slug="actualite-nationale").order_by('-last_update')[:instance.nb_last_post]
#
#         context.update({
#             'posts_inter': posts_internationals,
#             'posts_nation': posts_nationals,
#             'instance': instance,
#             'placeholder': placeholder
#         })
#         return context

class ArticleImportant(CMSPluginBase):

    model = EntryZiniaCmsPlugins
    name = u"Actualités importantes (acceuil)"
    render_template = "base/actualite_important.html"
    module = 'blog'

    def render(self, context, instance, placeholder):
        posts = Entry.objects.filter(categories__slug="important").order_by('-last_update')[:instance.nb_last_post]

        context.update({
            'posts': posts,
            'instance': instance,
            'placeholder': placeholder
        })
        return context


class AgendaPlugin(CMSPluginBase):
    module = 'Agenda'
    name = 'Dernier event'
    render_template = 'base/agenda_plugin.html'

    def render(self, context, instance, placeholder):
        events = Event.objects.filter(end__gt=datetime.datetime.today()).order_by('start')
        context['events'] = events
        return context

class SallePlugin(CMSPluginBase):
    model = ListeSalle
    name = "Liste des salles"
    render_template = "base/salles.html"
    module = 'salles'

    def render(self, context, instance, placeholder):
        """Update the context with plugin's data"""
        salles = Salle.objects.filter(pays=instance.pays).order_by('id')

        context.update({'salles': salles,
                        'object': instance,
                        'placeholder': placeholder})
        return context


class AllSallePlugin(CMSPluginBase):
    name = 'Toutes les salles'
    render_template = "base/all_salles.html"
    module = 'salles'

    def render(self, context, instance, placeholder):
        salles = Salle.objects.all()
        markers = u'['
        for x in salles:
            if x.longitude and x.latitude and x.marker():
                markers += x.marker() + u','
        markers = markers[:-1]
        markers += u']'
        context.update({'salles': salles,
                        'markers': markers})
        return context

# plugin_pool.register_plugin(ArticleInternaltionalNational)
plugin_pool.register_plugin(ArticleImportant)
plugin_pool.register_plugin(SallePlugin)
plugin_pool.register_plugin(AgendaPlugin)
plugin_pool.register_plugin(AllSallePlugin)
