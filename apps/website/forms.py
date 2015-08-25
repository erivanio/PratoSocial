# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail


class FormContact(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=50)
    message = forms.Field(widget=forms.Textarea)

    def send(self):
        title = 'Mensagem do site Prato Social - Contato'
        target = 'contato@pratosocial.com.br'
        text = """
        Nome: %(name)s
        E-mail: %(email)s
        Telefone: %(phone)s
        Assunto: %(message)s
        """ % self.cleaned_data

        send_mail(
            subject=title,
            message=text,
            from_email=target,
            recipient_list=[target],
            )