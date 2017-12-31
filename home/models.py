from django.db import models

# Create your models here.

class Visiteur(models.Model):
    mel = models.CharField(max_length=100, verbose_name="Mail")
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de visite")

    def __str__(self):
        return self.mel
