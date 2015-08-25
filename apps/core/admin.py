from daterange_filter.filter import DateRangeFilter
from django.contrib import admin
from django.db import models
from apps.core.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_superuser', 'get_recipes')
    search_fields = ['username', 'email', 'description']
    list_filter = [('created_date', DateRangeFilter), 'is_superuser', ('last_login', DateRangeFilter), 'state']

    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        qs = qs.annotate(models.Count('recipe'))
        return qs

    def get_recipes(self, obj):
        return obj.recipe__count
    get_recipes.short_description = u'Receitas'
    get_recipes.admin_order_field = 'recipe__count'

admin.site.register(User, UserAdmin)
