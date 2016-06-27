# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.contrib.auth.views import login

from django.views.generic import TemplateView
from oai.views import *

urlpatterns = patterns('',
        url(r'^$', TemplateView.as_view(template_name='oai/front.html'), name='front'),
        url(r'^tos$', TemplateView.as_view(template_name='oai/tos.html'), name='tos'),
        url(r'^'+OAI_ENDPOINT_NAME+'$', endpoint, name='oaiEndpoint'),
        url(r'^ctl$', controlPannel, name='controlPannel'),
        url(r'^login/$', login, {'template_name': 'admin/login.html'}),
        url(r'^source/(?P<pk>\d+)/updateformats/$', updateFormats, name='updateFormats'),
        url(r'^(?P<doi>10\..*)', get_doi, name='get_doi'),
        url(r'^(?P<doi>[a-z0-9]{3,})$', get_doi, name='get_doi'),
)
