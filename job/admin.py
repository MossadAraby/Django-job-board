from django.contrib import admin

# Register your models here.
from job.models import Jobs, categories, apply_job
admin.site.register(Jobs)
admin.site.register(categories)
admin.site.register(apply_job)
