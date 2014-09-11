from django.core.urlresolvers import reverse
from base.models import PaysModel

__author__ = 'paul'
from menus.base import NavigationNode
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from menus.menu_pool import menu_pool

class TestMenu(CMSAttachMenu):

    name = _("test menu")

    def get_nodes(self, request):
        nodes = []
        query_pays = PaysModel.objects.filter(salle__isnull=False).distinct()
        id = query_pays.count() + 1
        for i, pays in enumerate(query_pays):
            nodes.append(NavigationNode(pays.label, "/", i+1))
            for j, regroupement in enumerate(pays.regroupementsalle_set.all().distinct()):
                id += 1
                nodes.append(NavigationNode(regroupement.nom, reverse('liste_salle',
                                                                      kwargs={'regroupement': regroupement.id}),
                                            id, i+1))
        return nodes

menu_pool.register_menu(TestMenu)

