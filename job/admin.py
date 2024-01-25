from django.contrib import admin

# Register your models here.
from job.models import Jobs, categories
admin.site.register(Jobs)
admin.site.register(categories)
