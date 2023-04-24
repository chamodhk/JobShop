from ast import And
from multiprocessing import get_context
from turtle import title
from unicodedata import category
from django.shortcuts import render
from .models import Job
from django.views import generic
from django.db.models import Q
# Create your views here.

class HomeJobView(generic.ListView):
    model = Job
    context_object_name ="hot_jobs"
    
    ordering =  ["-views"]
    template_name = 'jobs/home_job.html'

    def get_queryset(self):
        queryset = Job.objects.all().order_by("-views")[:6]
        return queryset

class SearchResultsListView(generic.ListView):
    model = Job
    context_object_name = 'jobs'
    paginate_by = 50
    template_name = 'jobs/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        category = self.request.GET.get("category")

        
      
       
        jobs = Job.objects.filter(
            Q(title__icontains=query) | Q(location__icontains=query)|Q(employer__icontains=query)
        ).order_by("posted_date")

        if category:
           
            jobs = jobs.filter(category=category)
        else:
            pass

        for job in jobs:
            job.impressed()
    
        
        for job in jobs:
            
            job.impressed()
        
        return jobs


def JobView(request,pk):
    job = Job.objects.get(pk=pk)
    
    jobs = Job.objects.filter(
        tags__in=job.tags.all()
    ).distinct().exclude(pk=pk)
    print(jobs)
    

    return render(request,"jobs/job.html",context={'job':job,'jobs':jobs})

    
    
