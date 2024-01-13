from django.db import models
import os

class Veiculo(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='uploaded_image/', null=True, blank=True)

    def __str__(self):
        return self.nome
    
    def delete(self, *args, **kwargs):
        # Exclua a imagem associada ao objeto
        if self.foto:
            if os.path.isfile(self.foto.path):
                os.remove(self.foto.path)
        super().delete(*args, **kwargs)
        