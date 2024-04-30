from django.db import models


class Pokedex(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    leyend = models.CharField(max_length=100)
    level = models.IntegerField()
    image = models.ImageField(upload_to='imagenes_pokemon', blank=True, null=True)

    def __str__(self):
        return self.name
    

