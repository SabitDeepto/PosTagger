# from django.http import HttpResponse
from django.shortcuts import render, redirect

from pos.forms import WordForm, TestForm
from pos.models import Word


def home(request):
    form = WordForm(request.POST)

    if form.is_valid():
        list_of_words = form.cleaned_data.get('word').split(' ')
        list_of_pos = ['Noun', 'Pronoun', 'Verb']
        words = zip(list_of_words, list_of_pos)
        result = dict(words)
        print(result)
        return render(request, 'design.html', {'query': result, 'form': form})

    return render(request, 'design.html', {'form': form})


def test(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        age = form.cleaned_data.get("age")
        sex = form.cleaned_data.get("sex")
        if sex == 'Male':
            age = age * 5
        else:
            age = age * 10

        return render(request, 'index.html', {'age': age, 'form': form, 'sex': sex})
    return render(request, 'index.html', {'form': form})
