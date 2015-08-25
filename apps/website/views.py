# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView
from apps.website.forms import FormContact


class ContactView(TemplateView):
    template_name = 'contato.html'

    def post(self, request, *args, **kwargs):
        form = FormContact(request.POST)
        if form.is_valid():
            form.send()
            messages.success(self.request, 'Mensagem enviada com sucesso')
        if form.errors:
            messages.warning(self.request, 'Fomulário inválido')
        return redirect('contact')

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['form'] = FormContact()
        return context

