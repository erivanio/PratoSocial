# -*- coding: utf-8 -*-
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib import messages
from apps.recipe.models import Recipe, RecipeBook
from apps.core.forms import SigninForm, LoginForm, UserEditForm
from django.contrib.auth import authenticate, login, logout
from apps.core.models import User
from django.shortcuts import redirect, resolve_url
from django.http import Http404, HttpResponseRedirect
from apps.website.models import Slide
from django.utils.translation import ugettext as _


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['slides'] = Slide.objects.filter(status=True)
        context['recent_recipes'] = Recipe.objects.filter(status=True).order_by('-published_at')[:3]
        context['commented_recipes'] = Recipe.objects.annotate(comment_count=Count('comments')).filter(status=True).order_by('-comment_count')[:4]
        context['visited_recipes'] = Recipe.objects.filter(status=True).order_by('-visits')[:3]
        context['suggested_recipes'] = Recipe.objects.filter(sugestion_day=True).order_by('?')[:2]
        context['top_chefs'] = User.objects.filter(is_active=True).annotate(num_recipes=Count('recipe')).order_by('-num_recipes')[:2]
        context['form_login'] = LoginForm(prefix='login')
        context['form_signin'] = SigninForm(prefix='signin')

        return context


    def post(self, request):
        form_login = LoginForm(request.POST, prefix='login')
        form_signin = SigninForm(request.POST, prefix='signin')

        if form_login.is_valid():
            if request.POST.has_key('remember_me'):
                request.session.set_expiry(29030400)
            u = authenticate(email=form_login.cleaned_data['email'], password=form_login.cleaned_data['password'])
            if u is not None:
                if u.is_active:
                    login(request, u)
                    return redirect('dashboard', pk=u.pk)
            messages.error(self.request, 'Email ou senha inválidos')

        if form_signin.is_valid():
            if not User.objects.filter(email=form_signin['email'].value()).exists():
                form_signin.save()
                u = authenticate(email=form_signin.cleaned_data['email'], password=form_signin.cleaned_data['password1'])
                if u is not None:
                    if u.is_active:
                        login(request, u)
                        return redirect('dashboard', pk=u.pk)
            else:
                messages.error(self.request, 'Email já cadastrado')

        return redirect('home')


class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class DashboardDetailView(DetailView):
    model = User
    template_name = 'core/user_detail.html'


class UserRecipeBookListView(ListView):
    model = RecipeBook
    template_name = 'core/user_recipebook_list.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(UserRecipeBookListView, self).get_context_data(**kwargs)
        context['chef'] = User.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        q = self.request.GET.get('q')
        object_list = RecipeBook.objects.filter(status=True, user_id=self.kwargs['pk']).order_by('-name')

        if q:
            object_list = object_list.filter(name__icontains=q)

        return object_list


class UserRecipeListView(ListView):
    model = Recipe
    template_name = 'core/user_recipe_list.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(UserRecipeListView, self).get_context_data(**kwargs)
        context['chef'] = User.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        q = self.request.GET.get('q')
        recipebook_pk = self.request.GET.get('livro')
        object_list = Recipe.objects.filter(status=True, user_id=self.kwargs['pk']).order_by('-name')

        if q:
            object_list = object_list.filter(name__icontains=q)
        if recipebook_pk:
            object_list = Recipe.objects.filter(status=True).order_by('-name')
            recipebook = RecipeBook.objects.get(pk=recipebook_pk)
            object_list = object_list.filter(id__in=recipebook.recipes.all())

        return object_list


class RecipeBookRecipeListView(ListView):
    model = Recipe
    template_name = 'core/user_recipe_list.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(RecipeBookRecipeListView, self).get_context_data(**kwargs)
        context['chef'] = User.objects.get(pk=self.kwargs['pk'])
        context['recipebook'] = RecipeBook.objects.get(pk=self.kwargs['recipebook_pk'])
        return context

    def get_queryset(self):
        q = self.request.GET.get('q')
        recipebook = RecipeBook.objects.get(pk=self.kwargs['recipebook_pk'])
        object_list = Recipe.objects.filter(status=True, id__in=recipebook.recipes.all()).order_by('-name')

        if q:
            object_list = object_list.filter(name__icontains=q)

        return object_list


class UserListView(ListView):
    model = User
    template_name = 'core/user_list.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['top_chefs'] = User.objects.filter(is_active=True).annotate(num_recipes=Count('recipe'), num_recipe_book=Count('recipebook')).order_by('-num_recipes')[:2]
        context['visited_recipes'] = Recipe.objects.filter(status=True).order_by('-visits')[:2]
        return context

    def get_queryset(self):
        q = self.request.GET.get('q')
        letter = self.request.GET.get('letra')
        object_list = User.objects.filter(is_active=True).order_by('-username')

        if q:
            object_list = object_list.filter(username__icontains=q)
        if letter:
            object_list = object_list.filter(username__startswith=letter)

        return object_list


class UserEditView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'core/user_edit.html'

    def get_object(self, *args, **kwargs):
        object = super(UserEditView, self).get_object(*args, **kwargs)
        if object != self.request.user:
            raise Http404
        return object

    def get_success_url(self):
        messages.success(self.request, 'Perfil modificado com sucesso!')
        return u'/chefes/%d/' % self.object.pk


class UserDeleteView(DeleteView):
    model = User

    def get_object(self, queryset=None):
        obj = super(UserDeleteView, self).get_object()
        if not obj == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        messages.success(self.request, 'Usuário deletado com sucesso!')
        return '/'


class PasswordResetUnregister(TemplateView):
    template_name = 'registration/password_reset_unregister.html'


@csrf_protect
def password_reset(request, is_admin_site=False,
                   template_name='registration/password_reset_form.html',
                   email_template_name='registration/password_reset_email.html',
                   subject_template_name='registration/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=None,
                   current_app=None,
                   extra_context=None,
                   html_email_template_name=None):
    if post_reset_redirect is None:
        try:
            if User.objects.filter(email=request.POST['email']).exists():
                post_reset_redirect = reverse('password_reset_done')
            else:
                return redirect('password_reset_unregister')
        except:
            post_reset_redirect = reverse('password_reset_done')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    if request.method == "POST":
        form = password_reset_form(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                'html_email_template_name': html_email_template_name,
            }
            if is_admin_site:
                opts = dict(opts, domain_override=request.get_host())
            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = password_reset_form()
    context = {
        'form': form,
        'title': _('Password reset'),
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)
