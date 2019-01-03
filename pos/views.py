# from django.http import HttpResponse
from django.shortcuts import render, redirect

from pos.forms import WordForm, TestForm
from pos.models import Word


def test(request):
    form = WordForm(request.POST)
    if form.is_valid():
        if request.POST.get('q'):
            global a
            a = form.cleaned_data.get('word').split(' ')
            print("split:")
            print(a)
            print(type(a))
            return render(request, 'design.html', {'query': a, 'form': form})

        else:
            a = form.cleaned_data.get('word').split(' ')
            b = form.cleaned_data.get('pos')
            c = dict(zip(a, b))
            print(c)
            print(type(c))

    return render(request, 'design.html', {'form': form})
