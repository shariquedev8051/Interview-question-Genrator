from django.db import models
from tag_list import Tags_choices
# Create your models here.


class Programms(models.Model):

    Programms = models.TextField()
    Answer = models.TextField(blank=True, null=True)
    Link = models.URLField(blank=True, null=True)
    Tag = models.CharField(
        max_length=30, choices=Tags_choices, default='Python')
    company = models.CharField(blank=True, null=True ,max_length=50)

    def __str__(self):
        return f'{self.Programms}'
