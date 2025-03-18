from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    
    #add the public attribute by Ken, Mar 2025
    public = models.BooleanField(default=False)
    
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):

        return self.text

class Entry(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    #modified by Ken to allow users to submit rich contents
    content = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)

    #added entry owner attribute by Ken
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        
        #modified by Ken to allow users to submit rich contents
        return f"{self.content[:50]}..." 

