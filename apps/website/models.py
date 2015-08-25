# coding=utf-8
from datetime import datetime
from django.db import models

class SocialNetwork(models.Model):
    email = models.EmailField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    snapwidget = models.TextField(null=True, blank=True, help_text='Adicione o código gerado pelo site http://snapwidget.com, com layout: "4x2", responsive: "Yes"')

    def __unicode__(self):
        return 'Redes Sociais Prato Social'

    class Meta:
        verbose_name = "Rede Social"
        verbose_name_plural = "Redes Sociais"

class Slide(models.Model):
    class Meta:
        ordering = ('created_at',)

    photo = models.ImageField('Foto', upload_to='uploads/slide/', help_text='Imagem para o slide da página inicial, tamanho 1200x400')
    recipe = models.ForeignKey('recipe.Recipe', verbose_name='Receita', blank=True, null=True, help_text='Para associar uma receita ao slide.')
    link = models.URLField(null=True, blank=True, help_text='Para redirecionar a outra página.')
    status = models.BooleanField('Ativo?', default=True)
    created_at = models.DateTimeField(verbose_name='Data do Cadastro', blank=True, default=datetime.now)


    def __unicode__(self):
        return u'%s' % str(self.photo).split('/')[-1]



