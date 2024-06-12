# Generated by Django 4.1 on 2024-06-05 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('my_order', models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Элемент слайдера',
                'verbose_name_plural': 'Элементы слайдера',
                'ordering': ['my_order'],
            },
        ),
    ]
