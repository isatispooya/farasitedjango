from django.db import models
from django_summernote.fields import SummernoteTextField
from website.models import Domain 

class ContentDrop(models.Model):
    Title = models.CharField(max_length=500)
    Summer = SummernoteTextField()


    def __str__(self) :
        return f'{self.Title()}'
    

class TabVision (models.Model) :
    Title = models.CharField(max_length=200)
    Summer = SummernoteTextField()
    Domain = models.ForeignKey (Domain , to_field='domain' , on_delete=models.CASCADE)
    Contentdrop = models.ManyToManyField (    
    ContentDrop,
    related_name= 'content_drop', 
    blank=True, help_text= 'Specific content for tab vision.', 
    verbose_name = 'summernot for content' )

    def __str__(self):
        return f'{self.Title()}'