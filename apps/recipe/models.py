# -*- coding: utf-8 -*-
import string
import random
import urllib
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from django_comments import Comment
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageRatioField
from datetime import datetime
from django.core.files import File
import os
from taggit.managers import TaggableManager


def update_filename(instance, filename):
    date = datetime.today()
    if type(instance) is CommentWithPic:
        path = "uploads/comments/"+str(date.year)+"/"+str(date.month)+"/"
    elif type(instance) is Recipe or PhotoRecipe or PhotoInstagram:
        path = "uploads/receitas/"+str(date.year)+"/"+str(date.month)+"/"
    elif type(instance) is RecipeBook:
        path = "uploads/livro-receitas/"+str(date.year)+"/"+str(date.month)+"/"
    else:
        path = "uploads/outros/"
    fname = filename.split('.')
    format = slugify(fname[0]) + ''.join([random.SystemRandom().choice(''.join(string.digits)) for i in range(8)]) + '.' + fname[-1]
    return os.path.join(path, format)


class CommentWithPic(Comment):
    image = models.ImageField(upload_to=update_filename, null=True, blank=True)
    image_thumb = ImageRatioField('image', '135x100')

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def get_image_thumb(self):
        return get_thumbnailer(self.image).get_thumbnail({
            'size': (135, 100),
            'box': self.image_thumb,
            'crop': True,
            'detail': True,
            }).url


class Recipe(models.Model):
    user = models.ForeignKey('core.User')
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', help_text='Breve descrição da receita')
    ingredients = models.TextField('Ingredientes')
    method_of_preparation = models.TextField('Modo de preparo')
    time_of_preparation = models.CharField('Tempo de preparo', max_length=20)
    produce = models.CharField('Redimento', max_length=20)
    photo = models.ImageField('Foto', upload_to=update_filename, null=True, blank=True)
    photo_260x140 = ImageRatioField('photo', '260x140')
    photo_260x300 = ImageRatioField('photo', '260x300')
    photo_162x150 = ImageRatioField('photo', '162x150')
    photo_235x151 = ImageRatioField('photo', '235x151')
    photo_450x450 = ImageRatioField('photo', '450x450')
    slug = models.SlugField(max_length=150, blank=True)
    tags = TaggableManager()
    sugestion_day = models.BooleanField('Sugestão do dia', default=False)
    status = models.BooleanField(default=True)
    comments = generic.GenericRelation(Comment, object_id_field="object_pk")
    visits = models.IntegerField(default=0)
    published_at = models.DateTimeField(verbose_name='Data de Publicacao', default=datetime.now)

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    def __unicode__(self):
        return self.name

    def imageAdmin(self):
        if self.photo:
            im = get_thumbnailer(self.photo).get_thumbnail({'size': (135, 135), 'box': self.photo_162x150})
            return '<img src="{0}" />'.format(im.url)
        else:
            return 'Sem Imagem'

    imageAdmin.is_safe = True
    imageAdmin.allow_tags = True
    imageAdmin.short_description = u'Imagem'

    def get_image_260x140(self):
        return get_thumbnailer(self.photo).get_thumbnail({
            'size': (260, 240),
            'box': self.photo_260x140,
            'crop': True,
            'detail': True,
            }).url

    def get_image_260x300(self):
        return get_thumbnailer(self.photo).get_thumbnail({
            'size': (260, 300),
            'box': self.photo_260x300,
            'crop': True,
            'detail': True,
            }).url

    def get_image_162x150(self):
        return get_thumbnailer(self.photo).get_thumbnail({
            'size': (162, 150),
            'box': self.photo_162x150,
            'crop': True,
            'detail': True,
            }).url

    def get_image_235x151(self):
        return get_thumbnailer(self.photo).get_thumbnail({
            'size': (235, 151),
            'box': self.photo_235x151,
            'crop': True,
            'detail': True,
            }).url

    def get_image_450x450(self):
        return get_thumbnailer(self.photo).get_thumbnail({
            'size': (450, 450),
            'box': self.photo_450x450,
            'crop': True,
            'detail': True,
            }).url

class PhotoRecipe(models.Model):
    photo = models.ImageField(verbose_name="Foto", upload_to=update_filename, blank=True)
    photo_thumb = ImageRatioField('photo', '135x100')
    recipe = models.ForeignKey(Recipe, verbose_name="Receita")

    class Meta:
        verbose_name = 'Foto de Receita'
        verbose_name_plural = 'Fotos de Receitas'
        ordering = ['recipe']

    def __unicode__(self):
        return u'%s' % str(self.photo).split('/')[-1]

    def image_thumb(self):
        if self.photo:
            try:
                im = get_thumbnailer(self.photo).get_thumbnail({
                    'size': (135, 100),
                    'box': self.photo_thumb
                })
                return im.url
            except:
                return ''

        return ''

    def imagemAdmin(self):
        if self.photo:
            try:
                im = get_thumbnailer(self.photo).get_thumbnail({
                    'size': (135, 90),
                    'box': self.photo_thumb
                })
                return '<img src="{0}" />'.format(im.url)
            except:
                return ''
        return ''

    imagemAdmin.is_safe = True
    imagemAdmin.allow_tags = True
    imagemAdmin.short_description = u'Imagem'


class PhotoInstagram(models.Model):
    image_file = models.ImageField(verbose_name="Foto Instagram", upload_to=update_filename, blank=True)
    image_url = models.URLField()
    photo_thumb = ImageRatioField('image_file', '135x100')
    recipe = models.ForeignKey(Recipe, verbose_name="Receita")

    def save(self, *args, **kwargs):
        get_remote_image(self)

        super(PhotoInstagram, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Foto de Receita'
        verbose_name_plural = 'Fotos de Receitas'
        ordering = ['recipe']

    def __unicode__(self):
        return u'%s' % str(self.image_file).split('/')[-1]

    def image_thumb(self):
        if self.image_file:
            try:
                im = get_thumbnailer(self.image_file).get_thumbnail({
                    'size': (135, 100),
                    'box': self.photo_thumb
                })
                return im.url
            except:
                return ''

        return ''

    def imagemAdmin(self):
        if self.image_file:
            try:
                im = get_thumbnailer(self.image_file).get_thumbnail({
                    'size': (135, 90),
                    'box': self.photo_thumb
                })
                return '<img src="{0}" />'.format(im.url)
            except:
                return ''
        return ''

    imagemAdmin.is_safe = True
    imagemAdmin.allow_tags = True
    imagemAdmin.short_description = u'Imagem'


class PhotoFacebook(models.Model):
    image_file = models.ImageField(verbose_name="Foto Facebook", upload_to=update_filename, blank=True)
    image_url = models.URLField()
    photo_thumb = ImageRatioField('image_file', '135x100')
    recipe = models.ForeignKey(Recipe, verbose_name="Receita")

    def save(self, *args, **kwargs):
        get_remote_image(self)

        super(PhotoFacebook, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Foto de Receita'
        verbose_name_plural = 'Fotos de Receitas'
        ordering = ['recipe']

    def __unicode__(self):
        return u'%s' % str(self.image_file).split('/')[-1]

    def image_thumb(self):
        if self.image_file:
            try:
                im = get_thumbnailer(self.image_file).get_thumbnail({
                    'size': (135, 100),
                    'box': self.photo_thumb
                })
                return im.url
            except:
                return ''

        return ''

    def imagemAdmin(self):
        if self.image_file:
            try:
                im = get_thumbnailer(self.image_file).get_thumbnail({
                    'size': (135, 90),
                    'box': self.photo_thumb
                })
                return '<img src="{0}" />'.format(im.url)
            except:
                return ''
        return ''

    imagemAdmin.is_safe = True
    imagemAdmin.allow_tags = True
    imagemAdmin.short_description = u'Imagem'


def get_remote_image(self):
    if self.image_url and not self.image_file:
        result = urllib.urlretrieve(self.image_url)
        fname = self.image_url.split('/')[-1]
        fname = fname.split('?')[0]
        self.image_file.save(
                os.path.basename(fname),
                File(open(result[0]))
                )
        self.save()


class RecipeBook(models.Model):
    name = models.CharField('Nome', max_length=200)
    recipes = models.ManyToManyField(Recipe, verbose_name='Receitas', blank=True, null=True)
    photo = models.ImageField('Foto', upload_to=update_filename, blank=True, null=True)
    photo_thumb = ImageRatioField('photo', '190x190')
    description = models.TextField('Descrição', blank=True, null=True, help_text='Breve descrição da livro')
    user = models.ForeignKey('core.User', verbose_name='Usuário')
    status = models.BooleanField(default=True)

    def get_photo_thumb(self):
        return get_thumbnailer(self.photo).get_thumbnail({
            'size': (190, 190),
            'box': self.photo_thumb,
            'crop': True,
            'detail': True,
            }).url

    class Meta:
        ordering = ('name',)
        verbose_name = 'Livro de receita'
        verbose_name_plural = 'Livros de receitas'

    def __unicode__(self):
        return self.name


def recipe_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

signals.pre_save.connect(recipe_pre_save, sender=Recipe)