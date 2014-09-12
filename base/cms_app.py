# coding=utf-8
from __future__ import unicode_literals
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from menu import TestMenu


class BlogApp(CMSApp):
    name = 'blog'
    urls = ['zinnia.urls']
apphook_pool.register(BlogApp)


__author__ = 'paul'

class BaseApp(CMSApp):
    name = _("Salles")
    urls = ["base.urls"]
    menus = [TestMenu]
    app_name = 'base' \
               ''
apphook_pool.register(BaseApp)
