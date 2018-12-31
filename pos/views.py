# from django.http import HttpResponse
from django.shortcuts import render, redirect

from pos.forms import WordForm
from pos.models import Word


def home(request):
    form = WordForm(request.POST)
    test = []

    if form.is_valid():
        catch = [form.cleaned_data.get('word').split(' ')]
        for temp in catch:
            return render(request, 'design.html', {'query': temp, 'form': form})

    return render(request, 'design.html', {'form': form})

# def home(request):
#     form = WordForm(request.POST)
#
#     if form.is_valid():
#         global catch
#         catch = form.cleaned_data.get('word').split(' ')
#         for temp in catch:
#
#             print(type(temp))
#
#         return render(request, 'design.html', {'query': temp, 'form': form})
#
#     return render(request, 'design.html', {'form': form})
