from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    
    #add the public attribute by Ken
    public = models.BooleanField(default=False)
    
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):

        return self.text

class Entry(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    #modify by Ken to allow user to enter rich contents
    #text = models.TextField()
    content = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        
        #modify by Ken to allow user to enter rich contents
        #return f"{self.content.get('text', '')[:50]}..."
        return f"{self.content[:50]}..." 

