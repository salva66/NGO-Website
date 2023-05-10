from django.db import models

# Create your models here.

class Slides(models.Model):
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics')
    stittle = models.TextField()
    stext = models.TextField()

class Mission(models.Model):
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics/mission')
    mtext = models.TextField()

class Vision(models.Model):
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics/vision')
    vtext = models.TextField()

class Purpose(models.Model):
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics/purpose')
    ptext = models.TextField()

class Values(models.Model):
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics/values')
    vvtext = models.TextField()

class Pcauses(models.Model):
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics/PopularCauses')
    Ptittle = models.TextField()
    Ptext = models.TextField()
    Pdescr = models.TextField()

class Team(models.Model):
    Tname = models.CharField(max_length=100)
    Timg =models.ImageField(upload_to='pics/Team')
    Ttittle = models.TextField()

class About(models.Model):    
    Ptittle = models.TextField()
    Pdescr = models.TextField()   
    
class OutlookDets(models.Model):
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics/OutlookDets')
    Ptittle = models.TextField()
    Pdescr = models.TextField()

class ArticleDets(models.Model):
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics/ArticleDets')
    Atittle = models.TextField()
    Adescr = models.TextField()

class GalleryDets(models.Model):
    name = models.CharField(max_length=100)
    img =models.ImageField(upload_to='pics/GalleryDets')
    Atittle = models.TextField()

class Objectives(models.Model):
    Objective1 = models.TextField()
    Objective2 = models.TextField()
    Objective3 = models.TextField()
    Objective4 = models.TextField()
    Objective5 = models.TextField()
    