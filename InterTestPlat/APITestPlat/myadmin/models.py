from django.db import models
from django.contrib.auth.models import AbstractUser, User



# Create your models here.

# class User(models.Model):
#
#     username = models.CharField(max_length=100, unique=True)
#     passwd = models.CharField(max_length=50)
#     email = models.CharField(max_length=50, unique=True)
#     status = models.IntegerField(default=1)
#     create_time = models.DateTimeField(auto_now=True)
#     update_time = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'user'


#用户表，改用django 的方法AbstractUser
class UserFi(AbstractUser):

    '''
        用户表
    '''
    mobile = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
