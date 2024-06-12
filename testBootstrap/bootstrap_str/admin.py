from django.contrib import admin
from easy_thumbnails.files import get_thumbnailer

from .models import SliderItem
from adminsortable2.admin import SortableAdminMixin
from django.utils.safestring import mark_safe


@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['display_image', 'title', 'my_order']
    search_fields = ['title']

    def display_image(self, obj):
        if obj.image:
            thumbnail_url = get_thumbnailer(obj.thumbnail)['admin_thumbnail'].url
            return mark_safe('<img src="{}" width="50" height="50" />'.format(thumbnail_url))
        else:
            return 'Изображение недоступно'

    display_image.allow_tags = True
    display_image.short_description = 'Изображение'
