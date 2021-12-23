import json
import threading
import os

from auto_test.models import CaseList
from APITestPlat import settings
# windows系统需要做路径格式替换
BASE_DIR = str(settings.BASE_DIR).replace("\\", "/")
jsonFilePath = BASE_DIR + "/auto_test/caseJson/case_data_list.json"
cmdPath = BASE_DIR + "/auto_test/"


class CaseThread:

    def __init__(self, case_id, env_url):
        self.id = case_id
        self.env_url = env_url

    def w_json(self):
        data = {}
        case = CaseList.objects.get(id=self.id)
        # print(case, type(case))
        print(self.env_url, type(self.env_url))
        data[case.name] = {
            "name": case.name,
            "url": self.env_url + case.url,
            "header": case.re_header,
            "method": case.method,
            "param_type": case.param_type,
            "body": case.params,
            "assert_type": case.assert_type,
            "check_key": case.check_key,
            "check_value": case.check_value,
        }
        # print(case_data)
        case_data = json.dumps(data)
        # 永远都是一条数据？？
        with open(jsonFilePath, "w") as f:
            f.write(case_data)
        # 运行用例，生成测试报告
        run_cmd = "python " + cmdPath + "run.py"
        print("运行的命令", run_cmd)
        os.system(run_cmd)

    # def run_tasks(self):
    #     threads = []
    #     t1 = threading.Thread(target=self.w_json)
    #     threads.append(t1)
    #     for t in threads:
    #         t.start()
    #     for t in threads:
    #         t.join()

    def run(self):
        threads = []
        t = threading.Thread(target=self.w_json)
        threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
