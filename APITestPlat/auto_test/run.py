from APITestPlat import settings
from ExtentHTMLTestRunner import HTMLTestRunner
import unittest
import requests
# import ddt
import time
from ddt import ddt, unpack, file_data, data
import re
import ast

BASE_DIR = str(settings.BASE_DIR).replace("\\", "/")
jsonFilePath = BASE_DIR + "/auto_test/caseJson/case_data_list.json"
reportFilePath = BASE_DIR + "/auto_test/report/"


def replace_var():
    pass


class RelyData(object):
    token = None


@ddt
class ApiTest(unittest.TestCase):

    # urls = "5"
    @unpack
    @file_data(jsonFilePath)
    def test_case(self, **kwargs):
        # print 的内容会输出到最终的html报告stdo一栏中
        if kwargs.get('method') == "GET":
            r = requests.get(kwargs.get('url'))
            if kwargs.get('variable'):
                setattr(RelyData, kwargs.get('variable'), re.findall(kwargs.get('var_rules'), r.text)[0])
                print(getattr(RelyData, kwargs.get('variable')))
            self.stdo(r, kwargs)
        elif kwargs.get('method') == "POST":
            # kwargs['header']取到的值是字符串
            kwargs['header'] = ast.literal_eval(kwargs['header'])
            kwargs['header'] = self.getRelyData(kwargs['header'])
            header = {kwargs['header']["header_key"]: kwargs['header']["header_value"]}
            print(header)
            body = ast.literal_eval(kwargs.get('body'))
            body = self.getRelyData(body)
            kwargs['body'] = body
            # 判断个请求参数类型：
            r = requests.post(kwargs.get('url'), data=body, headers=header)
            self.stdo(r, kwargs)
        elif kwargs.get('method') == "DELETE":
            pass
        elif kwargs.get('method') == "PUT":
            pass
        else:
            print("请求方法错误")

    def stdo(self, r, kwargs):
        print("\n---用例请求参数---\n", "\n用例名:" + kwargs.get('name'), "\nURL:" + kwargs.get('url'), "\nMethod:",
              kwargs.get('method'), "\nHeader:", kwargs.get('header'), "\nparam_type:", kwargs.get('param_type'),
              "\nBody:", kwargs.get('body'), "\n---用例响应数据---\n", "\n响应头:" + str(r.headers),
              "\n响应码：", r.status_code, "\n响应内容：", r.text)

    def getRelyData(self, dict_data):
        for k, v in dict_data.items():
            if "$" in v:
                key = v.strip("$")
                value = getattr(RelyData, key)
                dict_data[k] = value
        return dict_data


    # def create_suite(self, dirs):
    #     #     print(dirs)
    #     #     suites = unittest.TestSuite()
    #     #     discover = unittest.defaultTestLoader.discover(dirs, "test_*.py")
    #     #     print(11)
    #     #     for test_suite in discover:
    #     #         for test_case in test_suite:
    #     #             print('10')
    #     #             suites.addTest(test_case)
    #     #     return suites

    # def run(self, suites):
    #     # runners = unittest.TextTestRunner(verbosity=2)
    #     # runners.run(suites)


if __name__ == "__main__":
    # case_dir = jsonFilePath
    # suite = ApiTest().create_suite(case_dir)

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ApiTest))
    # 怎样取到用例名字+时间戳作为报告的文件名？
    time = time.strftime("%Y%m%d-%H%M%S")
    filePath = reportFilePath + str(time) + '.html'
    with open(filePath, 'wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            title='接口',  # html的标题，报告的标题
            description='6666666666666666666:',
        )
        runner.run(suite)
    # 执行完在重命名report？？--设置全局变量不行？或者在取一次json文件
