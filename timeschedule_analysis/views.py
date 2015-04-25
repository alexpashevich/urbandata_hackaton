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
    # logger.info('get_all_bins function')
    bins = Bin.objects.all()
    bins_array = []
    for bin in Bin.objects.all():
        bin_dict = {}
        bin_dict['x_coordinate'] = bin.x_coordinate
        bin_dict['y_coordinate'] = bin.y_coordinate
        bin_dict['address'] = bin.address
        bin_dict['volume'] = bin.volume
        bin_dict['cur_filling'] = bin.cur_filling
        bins_array.append(bin_dict)
    # logger.info(bins_array)
    dump = json.dumps(bins_array)
    return HttpResponse(dump, content_type='application/json')

def send_new_bin(request):
    logger.info('send_new_bin function')
    return HttpResponse(json.dumps({'a': 1}), content_type='application/json')