from django.urls import path,include
from . import views

app_name = 'job'


urlpatterns = [
    path('', views.jobs_list,name='jobs_list'),
    
]
