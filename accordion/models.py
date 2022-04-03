from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=2000)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publisher")
    timestamp = models.DateTimeField(auto_now_add=True)

class Keyboard(models.Model):

    F = models.CharField(max_length=1, default='q')
    FS = models.CharField(max_length=1, default='w')
    G = models.CharField(max_length=1, default='e')
    GS = models.CharField(max_length=1, default='r')
    A = models.CharField(max_length=1, default='t')
    AS = models.CharField(max_length=1, default='y')
    B = models.CharField(max_length=1, default='u')

    C2 = models.CharField(max_length=1, default='i')
    CS2 = models.CharField(max_length=1, default='o')
    D2 = models.CharField(max_length=1, default='p')
    DS2 = models.CharField(max_length=1, default='a')
    E2 = models.CharField(max_length=1, default='s')
    F2 = models.CharField(max_length=1, default='d')
    FS2 = models.CharField(max_length=1, default='f')
    G2 = models.CharField(max_length=1, default='g')
    GS2 = models.CharField(max_length=1, default='h')
    A2 = models.CharField(max_length=1, default='j')
    AS2 = models.CharField(max_length=1, default='k')
    B2 = models.CharField(max_length=1, default='l')

    C3 = models.CharField(max_length=1, default='z')
    CS3 = models.CharField(max_length=1, default='x')
    D3 = models.CharField(max_length=1, default='c')
    DS3 = models.CharField(max_length=1, default='v')
    E3 = models.CharField(max_length=1, default='b')
    F3 = models.CharField(max_length=1, default='n')
    FS3 = models.CharField(max_length=1, default='m')
    G3 = models.CharField(max_length=1, default='1')
    GS3 = models.CharField(max_length=1, default='2')
    A3 = models.CharField(max_length=1, default='3')
    AS3 = models.CharField(max_length=1, default='4')
    B3 = models.CharField(max_length=1, default='5')

    #Stredella Bass System
    BassDmaj = models.CharField(max_length=1, default='6')
    BassD = models.CharField(max_length=1, default='7')
    BassA = models.CharField(max_length=1, default='8')
    BassAdom7 = models.CharField(max_length=1, default='9')
    BassE = models.CharField(max_length=1, default='0')


    changer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="changer")

