from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Audio

def audios(request):
    query = request.GET.get('q', '')

    if query:
        lista_audios = Audio.objects.filter(
            Q(titulo__icontains=query) |
            Q(genero__icontains=query)
        )
    else:
        lista_audios = Audio.objects.all()

    paginator = Paginator(lista_audios, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'audios.html', {
        'audios': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'q': query
    })
