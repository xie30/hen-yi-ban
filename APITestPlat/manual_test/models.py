from django.db import models

# Create your models here.


class InterfaceTest(models.Model):
    '''
        手动测试的接口保存下来:如果参数不是非必须的都要允许填空，用于测试异常情况
        设置表名？？
    '''
    file_name = models.CharField(max_length=100, unique=True)
    api_name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=200)
    method = models.CharField(max_length=15)
    headers = models.CharField(max_length=400, blank=True)
    params = models.CharField(max_length=1000, blank=True)
    params_type = models.CharField(max_length=20, blank=True)
    judge = models.CharField(max_length=200, blank=True)
    judge_type = models.CharField(max_length=30, blank=True)
    case_description = models.TextField(max_length=300, blank=True)
    creator = models.CharField(max_length=50, default='无名')
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

    class Meta:
        db_table= 'm_api'