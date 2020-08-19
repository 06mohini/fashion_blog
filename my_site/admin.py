from django.contrib import admin
from .models import Feedback

# Register your models here.
class FeedbackAdmin (admin.ModelAdmin) :
    list_display=['id','email']
    list_per_page=25
    list_filter=['email']
    list_display_links=['id','email']

admin.site.register(Feedback,FeedbackAdmin)    
