from django.db import models

# Create your models here.
class Handover(models.Model):
    title = models.CharField(max_length = 100)
    slug  = models.SlugField()
    domain = models.CharField(max_length = 20)
    body = models.TextField()
    sms = models.CharField(max_length = 10)
    date = models.DateTimeField(auto_now_add = True)
    #ticketNo = models.CharField(max_length = 10)
    # in add thumbnail
    # add in auther
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[0:50] + ' ...'
        
