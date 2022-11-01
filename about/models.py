from django.db import models

class santri(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

