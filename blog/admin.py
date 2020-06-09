from django.contrib import admin
from django.utils import timezone
from .models import ArticleCategories, Article, Comment


@admin.register(ArticleCategories)
class ArticleCategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'category']
    list_filter = ['title', 'pub_date', 'category']
    actions = ['copy_article']

    def copy_article(self, request, queryset):
        for item in queryset:
            item.title = item.title + ' (copy)'
            item.pub_date = timezone.now()
            item.pk = None
            item.save()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'article', 'created_on', 'active')
    list_filter = ('active', 'created_on', 'article')
    search_fields = ('name', 'email', 'body')
    actions = ['hide_comments']

    def hide_comments(self, request, queryset):
        queryset.update(active=False)


# admin.site.register(ArticleCategories, ArticleCategoriesAdmin)
# admin.site.register(Article, ArticleAdmin)
# admin.site.register(Comment, CommentAdmin)
