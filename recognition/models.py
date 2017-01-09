from __future__ import unicode_literals
from django.db import models

class RecognitionImage(models.Model):
    image = models.FileField(upload_to='profile/%Y/%m/%d')
    class Meta:
        ordering = ['-pk']
    def __str__(self):
        return str(self.id)