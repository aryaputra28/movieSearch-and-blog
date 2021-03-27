from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pengguna(models.Model):
    namalengkap = models.CharField(max_length=100)
    akun = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ".format(self.namalengkap)

class Blog(models.Model):
    judulBlog = models.CharField(max_length=400)
    isiBlog = models.TextField(max_length=20000)
    akun = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "{} ".format(self.judulBlog)
    