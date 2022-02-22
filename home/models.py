from django.db import models
from datetime import datetime
# Create your models here.



class Data(models.Model):
    name = models.CharField("نام و نام خانوادگی", max_length=100)
    title = models.CharField('عنوان', max_length=100)
    phone_number = models.CharField('شماره تماس', max_length=200)
    created_at = models.FloatField(default=datetime.now().timestamp())
    education = models.CharField('تحصیلات',max_length=100)
    
    def __str__(self):
        return self.name

    

