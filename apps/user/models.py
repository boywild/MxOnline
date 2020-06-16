from django.db import models
from datetime import datetime


# Create your models here.

class BaseModel(models.Model):
    add_date = models.DateField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        abstract = True


class UserProfile(BaseModel):
    GENDER_CHOICE = (
        ('male', '男'),
        ('female', '女')
    )
    nick_name = models.CharField(verbose_name='昵称', max_length=50, default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(verbose_name='性别', choices=GENDER_CHOICE, max_length=6, default='')
    address = models.CharField(verbose_name='地址', max_length=100, default='')
    mobile = models.CharField(verbose_name='手机', max_length=11)
    image = models.ImageField(verbose_name='图像', upload_to='head_image/%Y/%m', default='default.jpg')
