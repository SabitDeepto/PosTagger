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
            print(a)
            print(type(a))
            return render(request, 'design.html', {'query': a, 'form': form})

        else:
            for x in a:
                b = form.cleaned_data.get('pos')
                print(b)
                Word.objects.create(word=x, pos=b)
                return redirect('test')

    return render(request, 'design.html', {'form': form})
