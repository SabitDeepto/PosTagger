# from django.http import HttpResponse
from django.shortcuts import render, redirect

from pos.forms import WordForm, TestForm
from pos.models import Word


def home(request):
    form = WordForm(request.POST)

    if form.is_valid():
        list_of_words = form.cleaned_data.get('word').split(' ')
        for x in list_of_words:
            Word.objects.create(word=x)
        list_of_pos = [form.cleaned_data.get('pos')]

        words = zip(list_of_words, list_of_pos)
        result = dict(words)

        return render(request, 'design.html', {'query': list_of_words, 'form': form})

    return render(request, 'design.html', {'form': form})

# def some_view(request):
#     if request.method == 'POST':
#         text = request.POST.get('field_name')
#         if text:
#             for line in text.split('\n'):
#                 SomeModel.objects.create(field_name=line)


#
# def home(request):
#     form = WordForm(request.POST)
#
#     if form.is_valid():
#         list_of_words = form.cleaned_data.get('word').split(' ')
#         list_of_pos = [form.cleaned_data.get('pos')]
#
#         words = zip(list_of_words, list_of_pos)
#         result = dict(words)
#
#         print(len(list_of_words))
#         return render(request, 'design.html', {'query': list_of_words, 'form': form})
#
#     return render(request, 'design.html', {'form': form})
