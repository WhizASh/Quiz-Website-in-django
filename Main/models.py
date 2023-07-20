from django.db import models

# Create your models here.


class question(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)



class userProfiles(models.Model):
    username=models.CharField(max_length=100)
    test_id = models.CharField(max_length=10)
