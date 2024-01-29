from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = ('categories')


JOB_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"), 
    # ("2 Hour", "2 Hour"), 
)

# * ---------------- create folder "(jobs_images)>(image) consist of (Id_User.Extension_Image)" ------------------------------------------------
def upload_image(instance,filename):
    ImageName,extension = filename.split(".")
    return "jobs_images/%s.%s" % (instance.id,extension)
# * ----------------------------------------------------------------

class Jobs(models.Model):
    owner = models.ForeignKey(User, verbose_name=("Job_Owner"), on_delete=models.CASCADE)
    title = models.CharField(max_length=60, default=None)
    image = models.ImageField(upload_to=upload_image) # TODO: Use Function (upload_image)
    # location
    
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length= 1200,default=None)
    published_at = models.DateTimeField(auto_now=True) # published at a job
    Vacancy = models.IntegerField(default=1) # Number of employees required
    salary = models.IntegerField()
    experience = models.IntegerField(default=1) #experience years
    category = models.ForeignKey(categories, on_delete= models.CASCADE) 
    #! add "" >> "category" When Class ( Category ) after this class
    slug = models.SlugField(blank=True, null = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Jobs,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = ('Jobs')
        

class apply_job(models.Model):
    job = models.ForeignKey(Jobs, verbose_name=("Apply_Job"), on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    portfolio_url = models.URLField()
    cv =  models.FileField()
    cover_letter = models.TextField(max_length=600)
    
    
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = ('Apply Job')