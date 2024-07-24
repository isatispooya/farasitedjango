
from django.db import models

class Introduction(models.Model):
   Title = models.CharField(max_length=200)
   Description = models.CharField(max_length=2000) 
   Photo = models.ImageField(upload_to='static/images/')

   def __str__(self) :
        return f'{self.Title}'


class Content(models.Model):
   Name = models.CharField(max_length=200)
   Introduction = models.ManyToManyField(
        Introduction ,
        related_name='i_introduction',
        blank=True,
        help_text='Specific introduction for content.',
        verbose_name='introduction')
   
   def __str__(self) :
        return f'{self.Name}'

