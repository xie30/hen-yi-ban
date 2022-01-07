from APITestPlat import settings
from ExtentHTMLTestRunner import HTMLTestRunner
import unittest
import requests
# import ddt
import time
from ddt import ddt, unpack, file_data, data
import re
BASE_DIR = str(settings.BASE_DIR).replace("\\", "/")
jsonFilePath = BASE_DIR + "/auto_test/caseJson/case_data_list.json"
reportFilePath = BASE_DIR + "/auto_test/report/"


class RelyData(object):
    token = None


@ddt
class ApiTest(unittest.TestCase):

    # urls = "5"
    @unpack
    @file_data(jsonFilePath)
    def test_case(self, name, url, header, method, param_type, body, assert_type, check_key, check_value, variable,
                  var_rules):
        # print 的内容会输出到最终的html报告stdo一栏中
        if method == "GET":
            r = requests.get(url)
            # 响应没有输出在报告中？--可以显示，报告往下拉，空行太多了
            setattr(RelyData, variable, re.findall(var_rules, r.text)[0])
            print(getattr(RelyData, "token"))
            print("\n---用例请求参数---\n", "\n用例名:" + name, "URL:" + url, "\nMethod:"+method, "\nHeader:" + header,
                  "\nparam_type:" + param_type, "\nBody:" + body, "\n---用例响应数据---\n", "\n响应头:" + str(r.headers),
                  "\n响应码：", r.status_code, "\n响应内容：", r.text)
        elif method == "POST":
            r = requests.post(url, body)
            print(type(body))
            print("\n---用例请求参数---\n", "\n用例名:" + name, "URL:" + url, "\nMethod:" + method, "\nHeader:" + header,
                  "\nparam_type:" + param_type, "\nBody:" + body, "\n---用例响应数据---\n", "\n响应头:" + str(r.headers),
                  "\n响应码：", r.status_code, "\n响应内容：", r.text)
        elif method == "DELETE":
            pass
        elif method == "PUT":
            pass
        else:
            print("请求方法错误")

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

