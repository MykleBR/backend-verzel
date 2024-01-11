from django.db import models

class Veiculo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='uploaded_image/', null=True, blank=True)

    def __str__(self):
        return self.nome