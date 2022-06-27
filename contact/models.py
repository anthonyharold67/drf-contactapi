from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    gender= models.CharField(
        max_length=1,
        choices=[("F","Female"),("M","Male"),("O","Other")]
    )

    def __str__(self):
        return f"{self.username}-{self.phone_number}-{self.gender}"