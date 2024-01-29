from django.urls import path,include
from . import views

app_name = 'job'


urlpatterns = [
    path('', views.jobs_list,name='jobs_list'),
    path('add', views.add_job,name='add_job'), 
    # path('<int:id>', views.job_detail,name='job_detail'),
    path('<str:slug>', views.job_detail,name='job_detail'),
]
