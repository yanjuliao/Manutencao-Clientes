from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2) #max_digits significa quantidade de numeros e decimal_places é a quantidade dps da vírgula#
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name
