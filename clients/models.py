from django.db import models

class Client(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.PositiveIntegerField()
    salário = models.DecimalField(max_digits = 12, decimal_places = 2)
    intro = models.TextField(null = True, blank = True)
    foto = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.nome +" "+self.sobrenome