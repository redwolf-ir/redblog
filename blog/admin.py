from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublished', 'Category_to_str')
    list_filter = ('published', 'status')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug' : ('title', )}
    ordering = ['-status', '-published']


    def Category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])
    Category_to_str.short_description = 'دسته‌بندی'


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)