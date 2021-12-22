from APITestPlat import settings
from ExtentHTMLTestRunner import HTMLTestRunner
# ExtentHTMLTestRunner详解：https://www.cnblogs.com/liudinglong/p/13379045.html
import unittest
import requests
import ddt
from ddt import ddt, unpack, file_data, data
BASE_DIR = str(settings.BASE_DIR).replace("\\", "/")
jsonFilePath = BASE_DIR + "/auto_test/caseJson/case_data_list.json"
reportFilePath = BASE_DIR + "/auto_test/report/"


@ddt
class ApiTest(unittest.TestCase):
    @unpack
    @file_data(jsonFilePath)
    def test_case(self, url, header, method, param_type, body, assert_type, check_key, check_value):
        url = "https://ovh.ginolegaltech.com/" + url
        print(url, header, method, param_type, body, assert_type, check_key, check_value)
        if method == "GET":
            requests.get(url)
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
    filePath = reportFilePath + 'report.html'
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title='接口',  # html的标题，报告的标题
        description="用例执行"
    )
    runner.run(suite)
    fp.close()
