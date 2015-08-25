# -*- coding: utf-8 -*-
from __future__ import absolute_import
from audioop import reverse

from django import http
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.html import escape
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST

import django_comments
from django_comments import signals
from django_comments.views.utils import next_redirect, confirmation_view

from itertools import chain
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView
from easy_pdf.views import PDFTemplateView
from apps.core.models import User
from apps.recipe.forms import RecipeForm, RecipeBookForm, CommentFormWithPic
from apps.recipe.models import Recipe, RecipeBook, PhotoRecipe, PhotoInstagram, PhotoFacebook


class RecipePDFView(PDFTemplateView):
    model = Recipe
    template_name = "recipe/recipe_pdf.html"

    def get_context_data(self, **kwargs):
        context = super(RecipePDFView, self).get_context_data(**kwargs)
        if 'pk' in self.kwargs:
            context['recipe'] = Recipe.objects.get(pk=self.kwargs['pk'])

        return context


class RecipeBookPDFView(PDFTemplateView):
    model = Recipe
    template_name = "recipe/recipe_book_pdf.html"

    def get_context_data(self, **kwargs):
        context = super(RecipeBookPDFView, self).get_context_data(**kwargs)
        if 'pk' in self.kwargs:
            context['recipe_book'] = RecipeBook.objects.get(pk=self.kwargs['pk'])

        return context


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe/recipe_list.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)
        context['top_chefs'] = User.objects.filter(is_active=True).annotate(num_recipes=Count('recipe'), num_recipe_book=Count('recipebook')).order_by('-num_recipes')[:2]
        context['visited_recipes'] = Recipe.objects.filter(status=True).order_by('-visits')[:2]
        return context

    def get_queryset(self):
        q = self.request.GET.get('q')
        if 'visitadas' in self.request.path:
            object_list = Recipe.objects.filter(status=True).order_by('-visits')
        elif 'comentadas' in self.request.path:
            object_list = Recipe.objects.annotate(comment_count=Count('comments')).filter(status=True).order_by('-comment_count')
        else:
            object_list = Recipe.objects.filter(status=True).order_by('-published_at')
        if q:
            object_list = object_list.filter(Q(name__icontains=q) | Q(user__username__icontains=q) | Q(tags__name__in=[q]))

        return object_list

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(RecipeCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        recipe = Recipe()
        recipe.name = form.cleaned_data['name']
        recipe.description = form.cleaned_data['description']
        recipe.ingredients = form.cleaned_data['ingredients']
        recipe.method_of_preparation = form.cleaned_data['method_of_preparation']
        recipe.produce = form.cleaned_data['produce']
        recipe.time_of_preparation = form.cleaned_data['time_of_preparation']
        recipe.tags = form.cleaned_data['tags']
        recipe.status = True
        recipe.user = self.request.user
        recipe.save()
        file_list = form.cleaned_data['images']
        try:
            if file_list[0]:
                for photo in file_list:
                    photo_recipe = PhotoRecipe()
                    photo_recipe.photo = photo
                    photo_recipe.recipe = recipe
                    photo_recipe.save()
        except:
            pass
        try:
            instagram_photo_list = self.request.POST.getlist('photo_instagram[]')
            if instagram_photo_list[0]:
                for image_url in instagram_photo_list:
                    photo_insta = PhotoInstagram()
                    photo_insta.image_url = image_url
                    photo_insta.recipe = recipe
                    photo_insta.save()
        except:
            pass

        if recipe.photoinstagram_set.all():
            recipe.photo = recipe.photoinstagram_set.all()[0].image_file
            recipe.save()
        elif recipe.photofacebook_set.all():
            recipe.photo = recipe.photofacebook_set.all()[0].image_file
            recipe.save()
        elif recipe.photorecipe_set.all():
            recipe.photo = recipe.photorecipe_set.all()[0].photo
            recipe.save()


        messages.success(self.request, 'Receita criado com sucesso!')
        return redirect('dashboard', pk=recipe.user.pk)

    def form_invalid(self, form):
        if 'photo' in form.errors:
            messages.error(self.request, 'O campo foto de destaque é obrigatório.')
        else:
            messages.error(self.request, 'Os campos com * são obrigatórios.')
        return self.render_to_response(self.get_context_data(form=form))


class RecipeDetailView(DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        context['top_chefs'] = User.objects.filter(is_active=True).annotate(num_recipes=Count('recipe'), num_recipe_book=Count('recipebook')).order_by('-num_recipes')[:2]
        context['visited_recipes'] = Recipe.objects.filter(status=True).order_by('-visits')[:2]
        try:
            context['recipe_book_list'] = RecipeBook.objects.filter(user=self.request.user).order_by('-name')
        except:
            pass
        return context

    def get_object(self, queryset=None):
        object = super(RecipeDetailView, self).get_object()
        object.visits += 1
        object.save()
        return object


class RecipeEditView(UpdateView):
    model = Recipe
    form_class = RecipeForm

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(RecipeEditView, self).dispatch(*args, **kwargs)

    def get_object(self, *args, **kwargs):
        object = super(RecipeEditView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise Http404
        return object

    def form_valid(self, form):
        obj = form.save()
        file_list = form.cleaned_data['images']
        try:
            if file_list[0]:
                for photo in file_list:
                    photo_recipe = PhotoRecipe()
                    photo_recipe.photo = photo
                    photo_recipe.recipe = obj
                    photo_recipe.save()
        except:
            pass
        try:
            instagram_photo_list = self.request.POST.getlist('photo_instagram[]')
            if instagram_photo_list[0]:
                for image_url in instagram_photo_list:
                    photo_insta = PhotoInstagram()
                    photo_insta.image_url = image_url
                    photo_insta.recipe = obj
                    photo_insta.save()
        except:
            pass
        try:
            facebook_photo_list = self.request.POST.getlist('photo_facebook[]')
            if facebook_photo_list[0]:
                for image_url in facebook_photo_list:
                    photo_insta = PhotoFacebook()
                    photo_insta.image_url = image_url
                    photo_insta.recipe = obj
                    photo_insta.save()
        except:
            pass

        if obj.photoinstagram_set.all():
            obj.photo = obj.photoinstagram_set.all()[0].image_file
            obj.save()
        elif obj.photofacebook_set.all():
            obj.photo = obj.photofacebook_set.all()[0].image_file
            obj.save()
        elif obj.photorecipe_set.all():
            obj.photo = obj.photorecipe_set.all()[0].photo
            obj.save()

        messages.success(self.request, 'Receita modificada com sucesso!')
        return redirect('dashboard', pk=obj.user.pk)

    def form_invalid(self, form):
        if 'photo' in form.errors:
            messages.error(self.request, 'O campo foto de destaque é obrigatório.')
        else:
            messages.error(self.request, 'Os campos com * são obrigatórios.')
        return self.render_to_response(self.get_context_data(form=form))

class RecipeDeleteView(DeleteView):
    model = Recipe

    def get_object(self, queryset=None):
        obj = super(RecipeDeleteView, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        messages.success(self.request, 'Receita deletada com sucesso!')
        return u'/chefes/%d/' % self.object.user.pk


class RecipeBookCreateView(CreateView):
    model = RecipeBook
    form_class = RecipeBookForm

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(RecipeBookCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        recipe_book = RecipeBook()
        recipe_book.name = form.cleaned_data['name']
        recipe_book.description = form.cleaned_data['description']
        recipe_book.photo = form.cleaned_data['photo']
        recipe_book.status = True
        recipe_book.user = self.request.user
        recipe_book.save()
        messages.success(self.request, 'Livro de receitas criado com sucesso!')
        return redirect('dashboard', pk=recipe_book.user.pk)

    def form_invalid(self, form):
        if 'description' in form.errors:
            messages.error(self.request, 'O campo descrição é obrigatório.')
        return self.render_to_response(self.get_context_data(form=form))


class RecipeBookEditView(UpdateView):
    model = RecipeBook
    form_class = RecipeBookForm

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(RecipeBookEditView, self).dispatch(*args, **kwargs)

    def get_object(self, *args, **kwargs):
        object = super(RecipeBookEditView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise Http404
        return object

    def form_valid(self, form):
        obj = form.save()
        messages.success(self.request, 'Livro de receitas modificada com sucesso!')
        return redirect('dashboard', pk=obj.user.pk)

    def form_invalid(self, form):
        if 'description' in form.errors:
            messages.error(self.request, 'O campo descrição é obrigatório.')
        return self.render_to_response(self.get_context_data(form=form))

class RecipeBookDeleteView(DeleteView):
    model = RecipeBook

    def get_object(self, queryset=None):
        obj = super(RecipeBookDeleteView, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        messages.success(self.request, 'Livro de receitas deletado com sucesso!')
        return u'/chefes/%d/' % self.object.user.pk


class CommentPostBadRequest(http.HttpResponseBadRequest):
    """
    Response returned when a comment post is invalid. If ``DEBUG`` is on a
    nice-ish error message will be displayed (for debugging purposes), but in
    production mode a simple opaque 400 page will be displayed.
    """
    def __init__(self, why):
        super(CommentPostBadRequest, self).__init__()
        if settings.DEBUG:
            self.content = render_to_string("comments/400-debug.html", {"why": why})


@csrf_protect
@require_POST
def post_comment(request, next=None, using=None):
    """
    Post a comment.

    HTTP POST is required. If ``POST['submit'] == "preview"`` or if there are
    errors a preview template, ``comments/preview.html``, will be rendered.
    """
    # Fill out some initial data fields from an authenticated user, if present
    data = request.POST.copy()
    if request.user.is_authenticated():
        if not data.get('name', ''):
            data["name"] = request.user.get_full_name() or request.user.get_username()
        if not data.get('email', ''):
            data["email"] = request.user.email

    # Look up the object we're trying to comment about
    ctype = data.get("content_type")
    object_pk = data.get("object_pk")
    if ctype is None or object_pk is None:
        return CommentPostBadRequest("Missing content_type or object_pk field.")
    try:
        model = models.get_model(*ctype.split(".", 1))
        target = model._default_manager.using(using).get(pk=object_pk)
    except TypeError:
        return CommentPostBadRequest(
            "Invalid content_type value: %r" % escape(ctype))
    except AttributeError:
        return CommentPostBadRequest(
            "The given content-type %r does not resolve to a valid model." % \
                escape(ctype))
    except ObjectDoesNotExist:
        return CommentPostBadRequest(
            "No object matching content-type %r and object PK %r exists." % \
                (escape(ctype), escape(object_pk)))
    except (ValueError, ValidationError) as e:
        return CommentPostBadRequest(
            "Attempting go get content-type %r and object PK %r exists raised %s" % \
                (escape(ctype), escape(object_pk), e.__class__.__name__))

    # Do we want to preview the comment?
    preview = "preview" in data

    # Construct the comment form
    form = django_comments.get_form()(target, data=data)

    # Check security information
    if form.security_errors():
        return CommentPostBadRequest(
            "The comment form failed security verification: %s" % \
                escape(str(form.security_errors())))

    # If there are errors or if we requested a preview show the comment
    if form.errors or preview:
        template_list = [
            # These first two exist for purely historical reasons.
            # Django v1.0 and v1.1 allowed the underscore format for
            # preview templates, so we have to preserve that format.
            "comments/%s_%s_preview.html" % (model._meta.app_label, model._meta.module_name),
            "comments/%s_preview.html" % model._meta.app_label,
            # Now the usual directory based template hierarchy.
            "comments/%s/%s/preview.html" % (model._meta.app_label, model._meta.module_name),
            "comments/%s/preview.html" % model._meta.app_label,
            "comments/preview.html",
        ]
        return render_to_response(
            template_list, {
                "comment": form.data.get("comment", ""),
                "form": form,
                "next": data.get("next", next),
            },
            RequestContext(request, {})
        )

    # Otherwise create the comment
    comment = form.get_comment_object()
    comment.image = request.FILES.get("image", None)
    comment.ip_address = request.META.get("REMOTE_ADDR", None)
    if request.user.is_authenticated():
        comment.user = request.user

    # Signal that the comment is about to be saved
    responses = signals.comment_will_be_posted.send(
        sender=comment.__class__,
        comment=comment,
        request=request
    )

    for (receiver, response) in responses:
        if response == False:
            return CommentPostBadRequest(
                "comment_will_be_posted receiver %r killed the comment" % receiver.__name__)

    # Save the comment and signal that it was saved
    comment.save()
    signals.comment_was_posted.send(
        sender=comment.__class__,
        comment=comment,
        request=request
    )

    return next_redirect(request, fallback=next or 'comments-comment-done',
        c=comment._get_pk_val())

comment_done = confirmation_view(
    template="comments/posted.html",
    doc="""Display a "comment was posted" success page."""
)