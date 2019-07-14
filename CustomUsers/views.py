from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from .models import *
# from .forms import *

User = get_user_model()


def ProfilePage(request):
    profile = User.objects.get(id=request.user.id)
    return render(request, 'profile.html', context={'prof': profile})
