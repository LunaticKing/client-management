from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits = 12, decimal_places = 2)
    intro = models.TextField(null = True, blank = True)
    pfp = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.name +" "+self.surname