# from django.http import HttpResponse
from django.shortcuts import render, redirect

from pos.forms import WordForm, TestForm
from pos.models import Word


def test(request):
    form = WordForm(request.POST)

    if form.is_valid():
        list_of_words = form.cleaned_data.get('word').split(' ')
        for x in list_of_words:
            Word.objects.create(word=x)
        # list_of_pos = [form.cleaned_data.get('pos')]

        return render(request, 'index.html', {'query': list_of_words, 'form': form})

    return render(request, 'index.html', {'form': form})

