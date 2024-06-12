from django.shortcuts import render

from .models import SliderItem


def bootstrap_page_handler(request):
    context = {
        'sliders': SliderItem.objects.all(),
    }

    return render(request, 'index.html', context=context)
