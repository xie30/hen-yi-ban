from django.db import models

# Create your models here.

class RunEnv(models.Model):
    '''
    测试环境
    '''
    name = models.CharField(max_length=188,unique=True)
    host_url = models.CharField(max_length=1000,unique=True)
    env_description = models.CharField(max_length=2000)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class Projrct(models.Model):
    '''
    项目
    '''
    name = models.CharField(max_length=188,unique=True)
    p_description = models.CharField(max_length=2000)
    p_creator = models.CharField(max_length=100)
    p_tester = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class MoKuai(models.Model):
    '''
    模块
    '''
    #project_name
    name = models.CharField(max_length=200,unique=True)
    m_description = models.CharField(max_length=200)
    m_creator = models.CharField(max_length=100)
    m_tester = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class CaseList(models.Model):
    '''
    用例
    '''
    #多表关联？
    # project_name
    # model_name

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=188,unique=True)
    url = models.CharField(max_length=10000)
    method = models.CharField(max_length=20)
    re_header = models.TextField()
    param_type = models.CharField(max_length=15)
    params = models.CharField(max_length=10000)
    check = models.CharField(max_length=1000)
    check_type = models.CharField(max_length=15)
    case_description = models.TextField(blank=True)
    result = models.BooleanField(blank=True, null=True)
    creator = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    execution_time = models.DateTimeField() #如何每次执行的时候触发这个字段更新？
    #增加字段支持上传附件的接口？

class TestSuite(models.Model):
    '''
    测试用例集
    '''
    #project_name
    name = models.CharField(max_length=200,unique=True)
    #多个case,list的方式保存？
    # case_id =
    # case_name =
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)



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
