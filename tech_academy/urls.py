from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cohort/create/', views.create_cohort, name='create_cohort'),
    path('cohort/<int:pk>/', views.cohort_detail, name='cohort_detail'),
    path('native/list/', views.native_list, name='native_list'),
    path('native/add/', views.add_native, name='add_native'),
    path('native/<int:pk>/detail/', views.native_detail, name='native_detail'),
]
