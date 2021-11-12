from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Recipe(models.Model):
    rec_head=models.CharField('Recipe Name',max_length=200)
    rec_descrip=models.TextField('Description')
    rec_1img=models.ImageField('1st Image', upload_to='main/static/img/',null=True)
    rec_composition=models.TextField('Recipe composition')
    rec_recipe=models.TextField('Recipe')
    rec_category=models.CharField('Category', max_length=200)
    rec_timecook=models.CharField('Time to cook',max_length=200)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.rec_head

    def get_1img_url(self):
        return self.rec_1img.url.replace('main/','')
