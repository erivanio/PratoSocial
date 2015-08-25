from daterange_filter.filter import DateRangeFilter
from django.contrib import admin
from image_cropping import ImageCroppingMixin
from apps.recipe.models import Recipe, RecipeBook, CommentWithPic, PhotoRecipe, PhotoInstagram, PhotoFacebook
from django.contrib.admin import SimpleListFilter
from taggit.models import TaggedItem


class TaggitListFilter(SimpleListFilter):
  """
  A custom filter class that can be used to filter by taggit tags in the admin.
  """

  # Human-readable title which will be displayed in the
  # right admin sidebar just above the filter options.
  title = ('tags')

  # Parameter for the filter that will be used in the URL query.
  parameter_name = 'tag'

  def lookups(self, request, model_admin):
    """
    Returns a list of tuples. The first element in each tuple is the coded value
    for the option that will appear in the URL query. The second element is the
    human-readable name for the option that will appear in the right sidebar.
    """
    list = []
    tags = TaggedItem.tags_for(model_admin.model)
    for tag in tags:
      list.append( (tag.name, (tag.name)) )
    return list

  def queryset(self, request, queryset):
    """
    Returns the filtered queryset based on the value provided in the query
    string and retrievable via `self.value()`.
    """
    if self.value():
      return queryset.filter(tags__name__in=[self.value()])

def make_suggested(ModelAdmin, request, queryset):
    queryset.update(sugestion_day=True)
make_suggested.short_description = "Marcar como receita do dia"

def unmake_suggested(ModelAdmin, request, queryset):
    queryset.update(sugestion_day=False)
unmake_suggested.short_description = "Desmarcar receita do dia"


class CommentWithPicAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('user', 'comment')
    search_fields = ('user', 'comment')


class PhotosInline(ImageCroppingMixin, admin.StackedInline):
    model = PhotoRecipe
    extra = 1


class PhotosInstagramInline(ImageCroppingMixin, admin.StackedInline):
    model = PhotoInstagram
    extra = 1


class PhotosFacebookInline(ImageCroppingMixin, admin.StackedInline):
    model = PhotoFacebook
    extra = 1


class RecipeAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('imageAdmin', 'name', 'user', 'sugestion_day', 'visits', 'get_tags')
    search_fields = ['name', 'description', 'ingredients']
    list_filter = [('published_at', DateRangeFilter), 'sugestion_day', TaggitListFilter]
    inlines = [PhotosInline, PhotosInstagramInline, PhotosFacebookInline]
    actions = [make_suggested, unmake_suggested]
    def get_tags(self, recipe):
        tags = []
        for tag in recipe.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)
    get_tags.short_description = u'Tags'


admin.site.register(CommentWithPic, CommentWithPicAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeBook)
