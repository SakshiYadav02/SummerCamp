from django.contrib import admin

# Register your models here.
from .models import Program_Management,Feedback,JobDescription,CityEvent,ContactUs
admin.site.register(Program_Management),
admin.site.register(Feedback),
admin.site.register(JobDescription),
admin.site.register(CityEvent),
admin.site.register(ContactUs)