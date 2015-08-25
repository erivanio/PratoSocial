# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
import requests
from apps.core.models import User
from apps.recipe.models import RecipeBook, PhotoRecipe, PhotoInstagram, PhotoFacebook
from apps.recipe.models import Recipe
from annoying.decorators import ajax_request

@ajax_request
def add_recipe(request, recipe_pk=None, recipe_book_pk=None):
    recipe_book = RecipeBook.objects.get(id=recipe_book_pk)
    recipe = Recipe.objects.get(id=recipe_pk)
    if recipe_book.user == request.user:
        if recipe in recipe_book.recipes.all():
            messages.warning(request, 'Livro de receitas selecionado já possui esta receita')
        else:
            recipe_book.recipes.add(recipe)
            recipe_book.save()
            messages.success(request, 'Receita adicionada ao livro de receitas "%s"' % recipe_book.name)
    else:
        messages.warning(request, 'Livro de receitas inválido')


@ajax_request
def del_photo_recipe(request, photo_recipe_pk=None):
    photo_recipe = PhotoRecipe.objects.get(id=photo_recipe_pk)
    if photo_recipe.recipe.user == request.user:
        photo_recipe.delete()


@ajax_request
def del_photo_insta(request, photo_insta_pk=None):
    photo_insta = PhotoInstagram.objects.get(id=photo_insta_pk)
    if photo_insta.recipe.user == request.user:
        photo_insta.delete()


@ajax_request
def del_photo_face(request, photo_face_pk=None):
    photo_face = PhotoFacebook.objects.get(id=photo_face_pk)
    if photo_face.recipe.user == request.user:
        photo_face.delete()


@ajax_request
def get_photo_instagram(request):
    user = User.objects.get(pk=request.user.pk)
    msg = 'Não foi encontrada nenhuma foto no seu instagram com "#pratosocial".'
    photos = []
    try:
        social = user.social_auth.get(provider='instagram')
        user_id = social.uid
        response = requests.get(
            'https://api.instagram.com/v1/users/'+user_id+'/media/recent',
            params={'access_token': social.extra_data['access_token']}
        )
        while True:
            data = response.json()['data']
            for i in range(0, len(data)):
                if 'pratosocial' in data[i]['tags']:
                    photos.append(data[i]['images']['standard_resolution']['url'])
            try:
                next_url = response.json()['pagination']['next_url']
            except:
                break
            response = requests.get(next_url)
    except:
        msg = 'Associe uma conta do instagram ao seu perfil em configurações'

    return render_to_response('imagens_insta.html', {'photos': photos, 'msg': msg}, context_instance=RequestContext(request))

@ajax_request
def get_photo_facebook(request):
    user = User.objects.get(pk=request.user.pk)
    msg = 'Não foi encontrada nenhuma foto no seu facebook com "#pratosocial".'
    photos = []
    try:
        social = user.social_auth.get(provider='facebook')
        user_id = social.uid
        response = requests.get(
            'https://graph.facebook.com/'+user_id+'/photos/uploaded',
            params={'access_token': social.extra_data['access_token']}
        )
        while True:
            data = response.json()['data']
            for i in range(0, len(data)):
                try:
                    if '#pratosocial' in data[i]['name']:
                        photos.append(data[i]['source'])
                except:
                    pass
            try:
                next_url = response.json()['paging']['next']
            except:
                break
            response = requests.get(next_url)
    except:
        msg = 'Associe uma conta do facebook ao seu perfil em configurações'

    return render_to_response('imagens_face.html', {'photos_face': photos, 'msg': msg}, context_instance=RequestContext(request))