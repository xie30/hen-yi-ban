'''
需求分析：2021-07-07 author：daxian
接口测试自动化平台：
    --V1版本基于diango框架，利用template实现前端；
    --V2版本，基于django rest framework+一个简单的前端框架

前端功能模块：
1.一个类似postman平台的建单接口测试模块：手动测试
    --可以单独保存：分目录保存
    --也可以保存到接口自动化测试用例中

2.自动化测试功能：
    2-1.setting  全局配置模块
    2-2.project 项目模块
    2-3.case list 用例集
    2-4.test suite 测试集
    2-5.test plan 测试计划
    2-6.report 查看模块

3.用户登录页面：
    --用户要区分两种权限，一种是可以只查看和使用1中的功能，另外一种是可以增删改查
    --注册
    --修改密码
    --忘记密码。。。。

后台功能模块:
1.管理员后台

后端
1.模型设计
        --建两个应用：分别对应前端的手动测试和自动化测试的功能模块
    1-1.手动测试app的模型
        --model 1：文件目录
            文件名（唯一） 测试用例名 （唯一）
        --model 2:
            测试用例名
            接口url地址
            请求方法
            请求头
            参数--参数内容，参数类型
            断言--断言内容，断言类型
            测试用例详细描述
            创建者
            创建时间
            更新时间

    1-2.自动化测试app的模型
        --model 1：setting

        --model 2：project
            2-1. 项目：项目名称 项目描述 创建人 创建时间 更新时间
            2-2. 模块：所属项目 模块名称 模块描述 测试人员 开发人员 创建人 创建时间 更新时间

        --model 3：case list
            3-1. 用例ID，用例名称 所属项目 所属模块  创建人 测试人  创建时间 更新时间
            3-2. 用例ID，测试用例名 接口url地址 请求方法 请求头 参数--参数内容，参数类型 断言--断言内容，断言类型 测试用例详细描述
                最后一次执行结果

        --model 4：test suite
            4-1. 测试集名称 所属模块 测试用例 创建时间 更新时间

        --model 5：test plan
            5-1. 测试任务名称 测试任务描述 任务执行状态 关联用例 创建时间 更新时间

        --model 6：test report
            6-1. 任务名称 报告名称 错误用例 失败用例 成功用例 跳过用例 总用例数 运行时长 详细 创建时间

    1-3.用户模型
        3-1.用户名 密码 邮箱地址 用户状态 创建时间 更新时间

2.接口设计(V2)

'''