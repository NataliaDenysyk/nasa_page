from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from filer.fields.image import FilerImageField


class SliderItem(models.Model):
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Изображение')
    thumbnail = ThumbnailerImageField(upload_to='thumbnails', blank=True)
    title = models.CharField(max_length=100, verbose_name='Название')
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, db_index=True, verbose_name='Порядок')

    class Meta:
        verbose_name = 'Элемент слайдера'
        verbose_name_plural = 'Элементы слайдера'
        ordering = ['my_order']

