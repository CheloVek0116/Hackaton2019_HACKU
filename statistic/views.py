from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import biology, math, phisycs


@csrf_exempt
def stats(request):
    print(request.user)
    # new_request_link = request.POST['link']
    # all_links = list(biology.objects.get(user=request.user).values_list('link', flat=True)) + list(math.objects.get(user=request.user).values_list(
    #     'link', flat=True)) + list(phisycs.objects.get(user=request.user).values_list('link', flat=True))
    # if request.POST or new_request_link not in all_links:
    #     print(request.POST)
    #     biology.objects.create(
    #         title=request.POST['title'], link=new_request_link)

    return JsonResponse({})
