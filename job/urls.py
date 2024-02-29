from django.urls import path,include
from . import views
from . import api

app_name = 'job'


urlpatterns = [
    path('', views.jobs_list,name='jobs_list'),
    path('add', views.add_job,name='add_job'), 
    # path('<int:id>', views.job_detail,name='job_detail'),
    path('<str:slug>', views.job_detail,name='job_detail'),
    # path('/<int:id>/<slug:slug>/', views.job_detail,name='job_detail'),
    #  api
    path('api/jobs', api.jobs_list_api,name='jobs_list_api'), 
    path('api/jobs/<int:id>', api.job_detail_api,name='job_detail_api'), 
    
    # CBV
    path('api/cbv/jobs', api.JobsListApi_CBV.as_view(),name='JobsListApi_CBV'), 
    path('api/cbv/jobs-and-add-job', api.JobsListCreateApiView_CBV.as_view(),name='JobsListCreateApiView_CBV'), 
    
    path('api/cbv/jobs/<int:id>', api.JobDetail_CBV.as_view(),name='JobDetail_CBV'), 
    
    
]
