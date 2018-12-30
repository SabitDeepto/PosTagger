# from django.http import HttpResponse
from django.shortcuts import render, redirect

from pos.forms import WordForm


def home(request):
    form = WordForm(request.POST)

    if form.is_valid():
        global catch
        catch = form.cleaned_data.get('word').split(' ')

        return render(request, 'design.html', {'query': catch, 'form': form})

    return render(request, 'design.html')
