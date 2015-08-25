# -*- coding: utf-8 -*-
from datetime import datetime
import os
import random
import string
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils.text import slugify
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageRatioField
from apps.recipe.models import Recipe

UF_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
)

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password):
        user = self.create_user(username, email, password=password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

def update_filename(instance, filename):
    path = "uploads/user/"
    fname = filename.split('.')
    format = slugify(fname[0]) + ''.join([random.SystemRandom().choice(''.join(string.digits)) for i in range(8)]) + '.' + fname[-1]
    return os.path.join(path, format)

class User(AbstractBaseUser):
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    email = models.EmailField(verbose_name='Email', max_length=255, unique=True, db_index=True)
    username = models.CharField('Nome', max_length=50)
    is_active = models.BooleanField('Ativo?', default=True)
    is_member = models.BooleanField('Membro?', default=True)
    is_superuser = models.BooleanField('Administrador?', default=False)
    created_date = models.DateTimeField('Criado em', default=datetime.now)
    photo = models.ImageField('Foto', upload_to=update_filename, blank=True, null=True)
    photo_thumb = ImageRatioField('photo', '65x65')
    state = models.CharField('Estado', max_length=50, choices=UF_CHOICES, blank=True, null=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    def get_photo_thumb(self):
        return get_thumbnailer(self.photo).get_thumbnail({
            'size': (65, 65),
            'box': self.photo_thumb,
            'crop': True,
            'detail': True,
            }).url

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser
