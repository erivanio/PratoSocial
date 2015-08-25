# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from apps.core.views import DashboardDetailView, UserEditView, UserListView, UserRecipeBookListView, UserRecipeListView, \
    RecipeBookRecipeListView, UserDeleteView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', DashboardDetailView.as_view(), name='dashboard'),
    url(r'^editar/(?P<pk>\d+)/$', UserEditView.as_view(), name='edit_user'),
    url(r'^deletar/(?P<pk>\d+)/$', UserDeleteView.as_view(), name='user_delete'),
    url(r'^listagem/$', UserListView.as_view(), name='user_list'),
    url(r'^(?P<pk>\d+)/listagem-livros/$', UserRecipeBookListView.as_view(), name='user_recipebook_list'),
    url(r'^(?P<pk>\d+)/listagem-receitas/$', UserRecipeListView.as_view(), name='user_recipe_list'),
    url(r'^(?P<pk>\d+)/listagem-receitas/(?P<recipebook_pk>\d+)/$', RecipeBookRecipeListView.as_view(), name='recipebook_recipe_list'),

)
