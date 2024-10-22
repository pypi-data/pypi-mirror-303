import json
import logging
import requests
from zyjj_client_sdk.base.base import Base
from zyjj_client_sdk.base.entity import TaskStatus


class ApiService:
    def __init__(self, base: Base):
        self.__header = {
            "x-username": base.username,
            "x-password": base.password,
            "Content-Type": "application/json",
            "referer": "https://zyjj.cc"
        }
        self.__base = f"{base.host}/api/v1/client"
        self.__session = requests.session()
        self.__timeout = 5

    def __request(self, method: str, path: str, data: dict = None):
        url = f"{self.__base}/{path}"
        logging.info(f"request url {url}")
        res = None
        if method == "get":
            res = self.__session.get(url, timeout=self.__timeout, headers=self.__header)
        elif method == "put":
            res = self.__session.put(url, timeout=self.__timeout, data=json.dumps(data), headers=self.__header)
        elif method == "post":
            res = self.__session.post(url, timeout=self.__timeout, data=json.dumps(data), headers=self.__header)
        elif method == "delete":
            res = self.__session.delete(url, timeout=self.__timeout, headers=self.__header)
        if res is None:
            logging.info("[request] request res is none")
        elif res.status_code != 200:
            logging.info(f"[request] request status code is {res.status_code}, res is {res.text}")
            raise Exception("server error")
        else:
            res = res.json()
            if "code" in res and res["code"] != 0:
                raise Exception(res["msg"])
            else:
                return res["data"]
        return {}

    # 获取腾讯云token
    def could_get_tencent_token(self):
        return self.__request("get", "cloud/tencent/token")

    # 获取腾讯云cos秘钥信息
    def could_get_tencent_cos(self):
        return self.__request("get", "cloud/tencent/cos")

    # 获取阿里云oss秘钥
    def cloud_get_aliyun_oss(self):
        return self.__request("get", "cloud/aliyun/oss")

    # 获取火山语音信息
    def cloud_get_volcano_voice(self):
        return self.__request("get", "cloud/volcano/voice")

    # 获取MQTT
    def cloud_get_mqtt(self):
        return self.__request("get", f"cloud/mqtt/task")

    # 拉取任务
    def task_pull_task(self):
        return self.__request("get", "task/pull")

    # 拉取任务流程
    def task_pull_flow(self, task_type: int):
        return self.__request("get", f"flow/{task_type}")

    # 更新任务状态
    def task_update_task(
            self,
            task_id: str,
            status: TaskStatus = None,
            point_cost: float = None,
            output: str = None,
            extra: str = None
    ):
        data = {}
        if status is not None:
            data["status"] = status.value
        if output is not None:
            data["output"] = output
        if extra is not None:
            data["extra"] = extra
        if point_cost is not None:
            data["point_cost"] = point_cost
        return self.__request("put", f"task/{task_id}", data)

    # 获取用户积分
    def get_user_point(self, uid: str) -> int:
        return self.__request("get", f"point/user/{uid}", {})

    # 扣除用户积分
    def use_user_point(self, uid: str, name: str, point: float, desc='') -> bool:
        if len(desc) > 20:
            desc = f'{desc[:20]}...'
        logging.info(f"[api] {uid} use point {point}")
        try:
            self.__request("post", "point/deducting", {
                "uid": uid,
                "name": name,
                "point": int(point),
                "desc": desc,
            })
            return True
        except Exception as e:
            logging.error(f"[api] use_user_point error {e}")
            return False

    # 获取配置
    def get_config(self, key: str) -> str:
        return self.__request("get", f"config/{key}")["value"]

    # 上传流程日志
    def upload_flow_log(self, data):
        return self.__request("post", "flow/log", data)

    # 获取流程数据
    def get_entity_data(self, entity_id: str) -> dict:
        res = self.__request("get", f"entity/{entity_id}")
        return json.loads(res['data'])

    # 获取流程信息
    def get_entity_info(self, entity_id: str) -> dict:
        return self.__request("get", f"entity/{entity_id}")