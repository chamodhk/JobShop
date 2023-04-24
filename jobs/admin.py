from django.contrib import admin
from .models import Job
# Register your models here.


class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display =[
        'title',
        'employer'
    ]

admin.site.register(Job,JobAdmin)