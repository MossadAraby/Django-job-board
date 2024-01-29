from django.shortcuts import redirect, render
# import Models
from .models import Jobs, categories
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AddJob, ApplyJob

# Create your views here.
def jobs_list(request):
    jobs_list = Jobs.objects.all()
    paginator = Paginator(jobs_list, 3)  
    #TODO: Show 2 Jobs per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"jobs": page_obj}
    return render(request,'job/jobs_list.html', context)

# def job_detail(request, id):
#     job_detail = Jobs.objects.get(id=id)
#     context = {"job": job_detail}
#     return render(request,'job/job_detail.html', context)

def job_detail(request, slug):
    job_detail = Jobs.objects.get(slug=slug)
    
    if request.method=='POST':
        form = ApplyJob(request.POST,request.FILES)
        
        if form.is_valid():
            MyForm= form.save(commit=False)
            MyForm.job=job_detail
            MyForm.save()
    else:
        form = ApplyJob()
        
    context = {"job": job_detail,"Form_Apply": form}
    return render(request,'job/job_detail.html', context)


def add_job(request):
    if request.method=='POST':
        formNEWJob = AddJob(request.POST,request.FILES)
        
        if formNEWJob.is_valid():
            MyForm= formNEWJob.save(commit=False)
            MyForm.owner= request.user
            MyForm.save()
            return redirect(reverse('jobs:jobs_list'))
    else:
        formNEWJob = AddJob()
        
    return render(request,'job/add_job.html', {'add_job':formNEWJob})