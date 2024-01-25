from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    


JOB_TYPE = (
    ("Full TTime", "Full Time"),
    ("Part TTime", "Part Time"), 
)

class Jobs(models.Model):
    title = models.CharField(max_length=60, default=None)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length= 1200,default=None)
    published_at = models.DateTimeField(auto_now=True) # published at a job
    Vacancy = models.IntegerField(default=1) # Number of employees required
    salary = models.IntegerField()
    experience = models.IntegerField(default=1) #experience years
    category = models.ForeignKey(categories, on_delete= models.CASCADE) 
    #! add "" >> "category" When Class ( Category ) after this class
    
    def __str__(self):
        return self.title
    