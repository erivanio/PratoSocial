# -*- coding: utf-8 -*-
from django import forms
from apps.core.models import User


class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
    password1 = forms.CharField(required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, widget=forms.PasswordInput())

    def clean(self):
        password1 = self.data.get("signin-password1")
        password2 = self.data.get("signin-password2")

        if password1 and password1 != password2:
            raise forms.ValidationError("Senhas não conferem!")

        return self.cleaned_data

    def save(self, commit=True):
        user = super(SigninForm, self).save(commit=False)
        user.set_password(self.data["signin-password1"])
        user.is_active = True
        user.is_member = True
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label=('Email'))
    password = forms.CharField(label=('Password'), widget=forms.PasswordInput)
    remember_me = forms.CheckboxInput()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'photo', 'state']
    username = forms.CharField(label='Nome')