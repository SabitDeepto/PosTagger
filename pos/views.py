# from django.http import HttpResponse
from django.shortcuts import render, redirect

from pos.forms import WordForm


def home(request):
    form = WordForm(request.GET)
    if form.is_valid():
        global catch
        catch = form.cleaned_data.get('word').split(' ')
        return redirect('home')

    return render(request, 'design.html', {'form': form, 'query': catch})



