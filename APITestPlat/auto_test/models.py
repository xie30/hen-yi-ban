from django.db import models

# Create your models here.

class Setting(models.Model):
    '''
    测试的配置
    '''
    pass

class Projrct(models.Model):
    '''
    项目
    '''
    pass

class CaseList(models.Model):

    '''
    展示的用例列表
    '''
    #用例id---》主键、自动创建
    id = models.AutoField(primary_key=True)
    case_name = models.CharField(max_length=100)
    project = models.CharField(max_length=68)
    model = models.CharField(max_length=68)
    creator = models.CharField(max_length=20)
    tester = models.CharField(max_length=20)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

class CaseDetail(models.Model):
    '''
    执行的用例
    '''
    id = models.AutoField(primary_key=True)
    case_name = models.CharField(max_length=100)

    url = models.CharField(max_length=10000)
    method = models.CharField(max_length=20)
    re_header = models.TextField()
    param_type = models.CharField(max_length=16)
    params = models.CharField(max_length=10000)
    check = models.CharField(max_length=1000)
    check_type = models.CharField(max_length=15)
    case_description = models.TextField(blank=True)
    result = models.BooleanField(blank=True, default=NULL)

    execution_time = models.DateTimeField()
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)

class TestSuite(models.Model):
    '''
    测试用例集
    '''
    pass

class TestPlan(models.Model):
    '''
    测试定时任务
    '''
    pass

class TestReport(models.Model):
    '''
    测试报告
    '''
    pass
