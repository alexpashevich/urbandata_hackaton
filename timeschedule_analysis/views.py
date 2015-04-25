from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import json

import logging
from timeschedule_analysis.models import Bin, Sample, City

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
    logger.info('get_all_bins function')
    bins = Bin.objects.all()
    logger.info('bin received')
    # logger.info(JsonResponse({'a': 1}))
    # logger.info(HttpResponse(json.dumps({'a': 1}), content_type='application/json'))
    return JsonResponse(bins)
    # return HttpResponse(json.dumps({'a': 1}), content_type='application/json')

def send_new_bin(request):
    logger.info('send_new_bin function')
    logger.info(request.data)
    logger.info(request.data['x_coord'])
    return HttpResponse(json.dumps({'a': 1}), content_type='application/json')