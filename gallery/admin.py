from django.contrib import admin
from .models import Image, Gallery


class ImageInLine(admin.TabularInline):
    model = Image
    extra = 5


class GalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Related article', {'fields': ['article'], 'classes': ['collapse']}),
    ]
    inlines = [ImageInLine]
    list_display = ['title', 'article', 'created_on']
    list_filter = ['article', 'created_on']
    search_fields = ['article', 'title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'gallery', 'timestamp']
    list_filter = ['gallery', 'title', 'timestamp']


admin.site.register(Gallery, GalleryAdmin)