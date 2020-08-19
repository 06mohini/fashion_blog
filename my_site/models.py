from django.db import models

# Create your models here.
class Feedback(models.Model):
    email= models.EmailField(max_length=50)
    comment= models.TextField(max_length=1000)

    def __str__(self):
        return self.email