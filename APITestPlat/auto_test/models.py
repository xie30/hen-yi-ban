from django.db import models

# Create your models here.

class RunEnv(models.Model):
    '''
    测试环境
    '''
    name = models.CharField(max_length=188, unique=True)
    host_url = models.CharField(max_length=1000, unique=True)
    env_description = models.CharField(max_length=1000)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class Project(models.Model):
    '''
    项目
    '''
    name = models.CharField(max_length=188, unique=True)
    p_description = models.CharField(max_length=1000)
    p_creator = models.CharField(max_length=100)
    p_tester = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class MoKuai(models.Model):
    '''
    模块
    '''
    name = models.CharField(max_length=200, unique=True)
    m_description = models.CharField(max_length=200)
    m_creator = models.CharField(max_length=100)
    m_tester = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # models ---> project多对一
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "model"
        verbose_name_plural = "models"

class CaseList(models.Model):
    '''
    用例
    '''
    name = models.CharField(max_length=188, unique=True)
    url = models.CharField(max_length=10000)
    method = models.CharField(max_length=20)
    re_header = models.TextField()  #
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

    # case ---> project_name 多对一
    # case ---> model_name 多对一
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    model = models.ForeignKey("MoKuai", on_delete=models.CASCADE)
    #case --->suite 多对一
    suite = models.ForeignKey("TestSuite", on_delete=models.CASCADE)

class TestSuite(models.Model):
    '''
    测试用例集
    '''
    name = models.CharField(max_length=200, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # suite -->project_name多对一
    project = models.ForeignKey("Project", on_delete=models.CASCADE)

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
