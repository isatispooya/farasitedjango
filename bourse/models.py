from django.db import models
from website.models import Domain


# cards
class Card (models.Model) :
    Title = models.CharField(max_length=150)
    Description = models.CharField(max_length=500)

    def __str__(self):
        return self.Title

# main page for introductions of bourse buttons in isatispooya.com
class Sections (models.Model) :
    Title = models.CharField(max_length=300)
    Domain = models.ForeignKey(Domain , to_field='domain' , on_delete=models.CASCADE)
    