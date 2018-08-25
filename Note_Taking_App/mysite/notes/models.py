from django.db import models

# Create your models here.
class Note(models.Model):
	#The text of a note
    text = models.CharField(max_length=120)
    #The date of a note
    created = models.DateTimeField(auto_now_add=True)
    #The amount of unique words of a note (zero by default)
    u_words = models.IntegerField(default=0)