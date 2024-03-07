from django.contrib import admin
from .models import Category, Notes


#  admin.site.register(Category)
#  admin.site.register(Products)


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Notes)




