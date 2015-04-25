from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
import json

# from moocs.models import Mooc, Lesson, Module


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'dashboard.html')