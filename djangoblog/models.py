from django.db import models

class Handover(models.Model):
    title = models.CharField(max_lenght = 100)
    TT = models.CharField(max_length = 10)
    slug  = models.SlugField()
    domain = models.CharField(max_lenght = 20)
    body = models.TextField()
    sms = models.CharField(max_lenght = 10)
    date = models.DateTimeField(auto_now_add = True)
    # in add thumbnail
    # add in author
