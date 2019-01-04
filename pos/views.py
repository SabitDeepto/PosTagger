# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from pos.forms import WordForm, TestForm, RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("./")
    else:
        form = RegisterForm()
    return render(request, 'template/register.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {'form': form})
