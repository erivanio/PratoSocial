# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import logout


def social_user(backend, uid, user=None, *args, **kwargs):
    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        if user and social.user != user:
            messages.warning(backend.strategy.request, 'Este %s já está associado a outra conta.'%provider)
        elif not user:
            user = social.user
    return {'social': social,
            'user': user,
            'is_new': user is None,
            'new_association': False
    }
