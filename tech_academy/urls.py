from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/cohort/', views.create_cohort, name='create_cohort')
]
