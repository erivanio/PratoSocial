# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django_comments import CommentForm
from apps.recipe.models import Recipe, RecipeBook, CommentWithPic
from ckeditor.widgets import CKEditorWidget

from django.utils.translation import ugettext_lazy as _
from django import forms


class MultiFileInput(forms.FileInput):
    def render(self, name, value, attrs={}):
        attrs['multiple'] = 'multiple'
        return super(MultiFileInput, self).render(name, None, attrs=attrs)

    def value_from_datadict(self, data, files, name):
        if hasattr(files, 'getlist'):
            return files.getlist(name)
        else:
            return [files.get(name)]


class MultiFileField(forms.FileField):
    widget = MultiFileInput
    default_error_messages = {
        'min_num': u"Devem ser enviados no mínimo %(min_num)s arquivos (recebidos %(num_files)s).",
        'max_num': u"Devem ser enviados no máximo %(max_num)s arquivos (recebidos %(num_files)s).",
        'file_size': u"Arquivo: %(uploaded_file_name)s, excedeu o tamanho máximo permitido."
    }

    def __init__(self, *args, **kwargs):
        self.min_num = kwargs.pop('min_num', 0)
        self.max_num = kwargs.pop('max_num', None)
        self.maximum_file_size = kwargs.pop('maximum_file_size', None)
        super(MultiFileField, self).__init__(*args, **kwargs)

    def to_python(self, data):
        ret = []
        for item in data:
            ret.append(super(MultiFileField, self).to_python(item))
        return ret

    def validate(self, data):
        super(MultiFileField, self).validate(data)
        num_files = len(data)
        if len(data) and not data[0]:
            num_files = 0
        if num_files < self.min_num:
            raise ValidationError(self.error_messages['min_num'] % {'min_num': self.min_num, 'num_files': num_files})
            return
        elif self.max_num and  num_files > self.max_num:
            raise ValidationError(self.error_messages['max_num'] % {'max_num': self.max_num, 'num_files': num_files})
        for uploaded_file in data:
            try:
                if uploaded_file.size > self.maximum_file_size:
                    raise ValidationError(self.error_messages['file_size'] % { 'uploaded_file_name': uploaded_file.name})
            except:
                pass


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients', 'method_of_preparation', 'time_of_preparation', 'produce', 'tags']
    description = forms.CharField(widget=CKEditorWidget())
    ingredients = forms.CharField(widget=CKEditorWidget())
    method_of_preparation = forms.CharField(widget=CKEditorWidget())
    images = MultiFileField(max_num=10, maximum_file_size=1024*1024*5, required=False)


class RecipeBookForm(forms.ModelForm):
    class Meta:
        model = RecipeBook
        fields = ['name', 'photo', 'description']
    description = forms.CharField(widget=CKEditorWidget())


class CommentFormWithPic(CommentForm):
    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super(CommentFormWithPic, self).__init__(*args, **kwargs)

    def get_comment_model(self):
        return CommentWithPic

    def get_comment_create_data(self):
        data = super(CommentFormWithPic, self).get_comment_create_data()
        data['image'] = self.cleaned_data['image']
        return data