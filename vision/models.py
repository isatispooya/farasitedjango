from django.db import models
from django_summernote.fields import SummernoteTextField


class ContentDrop(models.Model):
    Title = models.CharField(max_length=500)
    Summer = SummernoteTextField()



    def __str__(self) :
        return f'{self.Title()}'


