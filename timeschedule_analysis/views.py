from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import json

import logging
# from moocs.models import Mooc, Lesson, Module

logger = logging.getLogger('testlogger')

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

def get_all_bins(request):
    # if request.method == 'GET':
    # bins = Bin.objects.all()
    logger.info('we are in get_all_bins function')
    logger.info(JsonResponse({'a': 1}))
    return JsonResponse({'a': 1})
    # return HttpResponse(json.dumps({'a': 1}), content_type='application/json')