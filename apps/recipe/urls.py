# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from apps.core.views import UserRecipeListView
from apps.recipe.views import RecipeDetailView, RecipeListView, RecipeEditView, RecipeBookCreateView, RecipeCreateView, RecipeDeleteView, RecipeBookDeleteView, RecipePDFView, RecipeBookPDFView, \
    RecipeBookEditView

urlpatterns = patterns('',
    url(r'^$', RecipeListView.as_view(), name='recipe_list'),
    url(r'^deleta/receita/(?P<pk>\d+)/$', RecipeDeleteView.as_view(), name='recipe_delete'),
    url(r'^deleta/livro/(?P<pk>\d+)/$', RecipeBookDeleteView.as_view(), name='recipe_book_delete'),
    url(r'^recentes/$', RecipeListView.as_view(), name='recipe_recent_list'),
    url(r'^comentadas/$', RecipeListView.as_view(), name='recipe_comment_list'),
    url(r'^visitadas/$', RecipeListView.as_view(), name='recipe_visit_list'),
    url(r'^detalhe/(?P<slug>[\w_-]+)-(?P<pk>\d+)/$', RecipeDetailView.as_view(), name='recipe_detail'),
    url(r'^nova/$', RecipeCreateView.as_view(), name='new_recipe'),
    url(r'^editar/(?P<slug>[\w_-]+)-(?P<pk>\d+)/$', RecipeEditView.as_view(), name='edit_recipe'),
    url(r'^livro-de-receitas/$', RecipeBookCreateView.as_view(), name='new_recipe_book'),
    url(r'^livro-de-receitas/editar/(?P<pk>\d+)/$', RecipeBookEditView.as_view(), name='recipebook_edit'),
    url(r'^livro-de-receitas/(?P<pk>\d+)/$', UserRecipeListView.as_view(), name='recipe_book_detail'),
    url(r'^adiciona-receita/(?P<recipe_pk>\d+)/(?P<recipe_book_pk>\d+)/$', 'apps.recipe.ajax.add_recipe', name='add_recipe'),
    url(r'^deletar-foto-receita/(?P<photo_recipe_pk>\d+)/$', 'apps.recipe.ajax.del_photo_recipe', name='del_photo_recipe'),
    url(r'^deletar-foto-instagram-receita/(?P<photo_insta_pk>\d+)/$', 'apps.recipe.ajax.del_photo_insta', name='del_photo_insta'),
    url(r'^deletar-foto-facebook-receita/(?P<photo_face_pk>\d+)/$', 'apps.recipe.ajax.del_photo_face', name='del_photo_face'),
    url(r'^receita-pdf/(?P<pk>\d+)/$', RecipePDFView.as_view(), name="recipe_pdf"),
    url(r'^livro-pdf/(?P<pk>\d+)/$', RecipeBookPDFView.as_view(), name="recipe_book_pdf"),
    url(r'^get-photos-instagram/$', 'apps.recipe.ajax.get_photo_instagram', name='get_photo_instagram'),
    url(r'^get-photos-facebook/$', 'apps.recipe.ajax.get_photo_facebook', name='get_photo_facebook'),

)
