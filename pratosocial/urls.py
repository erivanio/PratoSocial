# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.core.views import HomeView, LogoutView
from apps.website.views import ContactView
from pratosocial import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^chefes/', include('apps.core.urls')),
    url(r'^receitas/', include('apps.recipe.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/post/$', 'apps.recipe.views.post_comment'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^contato/', ContactView.as_view(), name='contact'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    # url('', include('django.contrib.auth.urls', namespace='auth'))

)
# Arquivos estáticos e de media
urlpatterns += patterns('',
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^ckeditor/', include('ckeditor.urls')),
)

admin.site.site_header = 'Prato Social'

