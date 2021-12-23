from APITestPlat import settings
from ExtentHTMLTestRunner import HTMLTestRunner
# ExtentHTMLTestRunner详解：https://www.cnblogs.com/liudinglong/p/13379045.html
import unittest
import requests
# import ddt
import time
from ddt import ddt, unpack, file_data, data
BASE_DIR = str(settings.BASE_DIR).replace("\\", "/")
jsonFilePath = BASE_DIR + "/auto_test/caseJson/case_data_list.json"
reportFilePath = BASE_DIR + "/auto_test/report/"


@ddt
class ApiTest(unittest.TestCase):

    # urls = "5"
    @unpack
    @file_data(jsonFilePath)
    def test_case(self, name, url, header, method, param_type, body, assert_type, check_key, check_value):
        # print 的内容会输出到最终的html报告stdo一栏中
        # print("\n---用例请求参数---\n", "URL:" + url, "\n请求方法:"+method, "\n请求头："+header, "\n请求参数类型："+param_type,
        #       "\n请求体："+body, "\n断言方式："+assert_type, "\n断言key："+check_key, "\n断言value："+check_value)
        if method == "GET":
            r = requests.get(url)
            print("\n---用例请求参数---\n", "URL:" + url)
            # 响应没有输出在报告中？
            print(r.text)
            print("响应："+str(r))
        elif method == "POST":
            pass
        elif method == "DELETE":
            pass
        elif method == "PUT":
            pass
        else:
            print("请求方法错误")


if __name__ == "__main__":
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

