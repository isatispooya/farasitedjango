from django.db import models
from django_summernote.fields import SummernoteTextField


class ContextDrop(models.model):
    title = models.CharField(max_length=500)
    summer = SummernoteTextField()


    def __str__(self) :
        return f'{self.title()}'


