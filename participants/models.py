from django.db import models

class People(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField()
    father_name=models.CharField(max_length=150)
    MY_CHOICES = [
        ('Song', 'Song'),
        ('Dance', 'Dance'),
        ('Skit', 'Skit'),
        ('Mimicry', 'Mimicry'),
        ('Mono Act', 'Mono Act'),
    ]
    item = models.CharField(max_length=50, choices=MY_CHOICES)
    ctgry = [
        ('Single', 'Single'),
        ('Group', 'Group'),
    ]
    
    category=models.CharField(max_length=50, choices=ctgry, default='Single')
    sts = [
        ('Pending', 'Pending'),
        ('Finished', 'Finished'),
        ('Cancelled', 'Cancelled'),
    ]
    status=models.CharField(max_length=50, choices=sts, default='Pending')
    def __str__(self):
        return self.name