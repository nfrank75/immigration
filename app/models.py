from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    message = models.TextField()
    sujet = models.CharField(max_length=100)

    def __str__(self):
        return self.name