from django.urls import path

from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:pk>', views.job_detail, name='job_detail'),
]
