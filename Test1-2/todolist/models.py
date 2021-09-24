from django.db import models

# Create your models here.
class Task(models.Model):
    # id = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    body = models.TextField()
    cre_dtm = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title