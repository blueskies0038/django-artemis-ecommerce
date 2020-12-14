from django.contrib import admin
from django.utils.html import mark_safe
from .models import *

class PhotoInline(admin.TabularInline):
    model = CollectionImage

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)

@admin.register(CollectionImage)
class CollectionImageAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.image.url}" />')

    get_thumbnail.short_description = "Thumbnail"

@admin.register(CollectionPreview)
class CollectionPreviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.image.url}" />')

    get_thumbnail.short_description = "Thumbnail"