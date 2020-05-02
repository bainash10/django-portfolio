from django.shortcuts import render, get_object_or_404
from .models import Job


def home(request):
    jobs = Job.objects.all()
    context = {
        'jobs' : jobs
    }
    return render(request, 'jobs/index.html', context)


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    context = {
        'job': job
    }
    return render(request, 'jobs/detail.html', context)