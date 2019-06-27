from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    def __str__(self):
        return self.title
        
#    def summary(self):
#        return self.body[:100]


class Person(models.Model):
    subject = models.CharField(max_length=30)
    professor = models.CharField(max_length=30)
    def __str__(self):
            return self.subject + "(" + self.professor + ")"