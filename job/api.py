#  Views
from .models import Jobs
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
# ############

#* Return a list of jobs (With Functions)
@api_view(['GET'])
def jobs_list_api(request):
    all_jobs = Jobs.objects.all()
    data = JobSerializer(all_jobs,many=True).data
    return Response({'data':data})


#* Return a one job detail (With Functions)
@api_view(['GET'])
def job_detail_api(request, id):
    Job_Detail = Jobs.objects.get(id=id)
    data = JobSerializer(Job_Detail).data
    return Response({'data':data})

#* Return a list of jobs (With class based views)
class JobsListApi_CBV(generics.ListAPIView):
    # model = Jobs
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer

#* Return a list of jobs and add a Job (With class based views)
class JobsListCreateApiView_CBV(generics.ListCreateAPIView):
    # model = Jobs
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer


#* Return a one job detail and update this (With class based views)
class JobDetail_CBV(generics.RetrieveUpdateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    
    lookup_field = 'id'
    