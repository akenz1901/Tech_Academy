from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

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
            return redirect('cohort_detail', pk=cohort.pk)
    else:
        form = CohortForm()
        return render(request, 'blog/new_cohort.html', {'form': form})


def cohort_detail(request, pk):
    cohort = get_object_or_404(Cohort, pk=pk)
    return render(request, 'blog/cohort_description.html', {'cohort': cohort})


def native_list(request):
    natives = Native.objects.filter(date_added__lte=timezone.now()).order_by("date_added")
    return render(request, 'blog/native_list.html', {'natives': natives})


def add_native(request):
    if request.method == 'POST':
        form = NativeForm(request.POST, request.FILES)
        if form.is_valid():
            native = form.save(commit=False)
            native.date_added = timezone.now()
            native.save()
            return redirect('native_list')
    else:
        form = NativeForm()
    return render(request, 'blog/add_native.html', {'form': form})


def native_detail(request, pk):
    native = get_object_or_404(Native, pk=pk)
    return render(request, 'blog/native_detail.html', {'native': native})
