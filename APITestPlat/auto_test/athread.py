import json
import threading
import os

from auto_test.models import CaseList
from APITestPlat import settings
from auto_test.run import RelyData

# windows系统需要做路径格式替换
BASE_DIR = str(settings.BASE_DIR).replace("\\", "/")
jsonFilePath = BASE_DIR + "/auto_test/caseJson/case_data_list.json"
cmdPath = BASE_DIR + "/auto_test/"


def w_jsons(data):
    # print(case_data)
    case_data = json.dumps(data)
    # 永远都是一条数据？？
    with open(jsonFilePath, "w") as f:
        f.write(case_data)


class CaseThread(RelyData):

    def __init__(self, case_id, env_url):
        self.id = case_id
        self.env_url = env_url

    def j(self, case):
        data = {case.name: {
            "name": case.name,
            "url": self.env_url + case.url,
            "header": case.re_header,
            "method": case.method,
            "param_type": case.param_type,
            "body": case.params,
            "assert_type": case.assert_type,
            "check_key": case.check_key,
            "check_value": case.check_value,
            "variable": case.variable,
            "var_rules": case.var_rules
        }}
        return data

    def w_json(self):
        case = CaseList.objects.get(id=self.id)
        # print(case.include)
        if case.include != 'None':
            case1 = CaseList.objects.get(id=case.include)
            case1_data = self.j(case1)
            case0_data = self.j(case)
            case = case1_data.copy()
            case.update(case0_data)
            # print(type(case), case)
            # 单个用例且有前置用例
            w_jsons(case)
            self.run_cmd()
            print("2222225555", getattr(RelyData, "token"))
            return
        # print("111", getattr(RelyData, "token"))
        # 单个用例且无前置用例执行
        w_jsons(self.j(case))
        self.run_cmd()

    @staticmethod
    def run_cmd():
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
