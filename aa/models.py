from django.db import models
#makemigrations - Create Changes and store in a file
# migrate - apply the pending changes created by makemigrations 
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    desc = models.TextField(max_length=120)
    date = models.DateField()

    def __str__(self):
        return self.name