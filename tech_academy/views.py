from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CohortForm, NativeForm
from .models import Cohort, Native
from django.utils import timezone


def home(request):
    cohorts = Cohort.objects.filter(date_created__lte=timezone.now()).order_by("date_created")
    return render(request, 'blog/home.html', {"cohorts": cohorts})


def create_cohort(request):
    if request.method == 'POST':
        form = CohortForm(request.POST)
        if form.is_valid():
            cohort = form.save(commit=False)
            cohort.author = request.user
            cohort.date_created = timezone.now()
            cohort.save()
            return redirect(request, '')
    else:
        form = CohortForm()
        return render(request, 'blog/new_cohort.html', {'form': form})


def native_list(request):
    return render(request, '')


def add_native(request):
    return render(request, '')
