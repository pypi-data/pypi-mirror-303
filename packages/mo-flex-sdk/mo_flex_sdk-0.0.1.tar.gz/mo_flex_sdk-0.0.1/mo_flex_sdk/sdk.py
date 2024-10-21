"""sdk"""
import logging
from datetime import datetime, timedelta
import time
import socket
import requests


class ImageWorker:
    """
    镜像处理
    """

    def __init__(
            self,
            service_code,
            platform_code
    ):
        self.service_code = service_code
        self.platform_code = platform_code
        self.server_url = "https://dev.ali-fc.mozigu.net/momo/mo_flex_task"

    def _pick_task(self):
        url = (
            f'{self.server_url}/task_pick'
            f'?service_code={self.service_code}'
            f'&platform_code={self.platform_code}'
        )
        gethostname = socket.gethostname()
        headers = {
            "gethostname": gethostname,
        }
        task_queue = requests.get(
            url,
            headers=headers,
            timeout=10
        ).json()
        if not task_queue:
            logging.info("队列为空")
            time.sleep(3)
            return {}
        task = task_queue
        task_id = task.get('_id')
        params = task.get('params', {})
        return {
            "task_id": task_id,
            "params": params
        }

    def _update_task(
            self,
            task_id,
            task_start_time,
            task_end_time,
            param
    ):
        """更新任务"""
        url = f'{self.server_url}/task/{task_id}'
        requests.put(url, json={
                "status": param.get("status"),
                "message": param.get("message"),
                "result": param.get("result", {}),
                "start_time": task_start_time.isoformat(),
                "end_time": task_end_time.isoformat()
            }, timeout=10
        )

    def work(self, work, delay=5):
        """执行自定义方法"""
        end_time = datetime.now() + timedelta(minutes=delay)
        while datetime.now() < end_time:
            task = self._pick_task()
            print('task', task)
            if task:
                task_start_time = datetime.now()
                result = work(**task)
                task_end_time = datetime.now()
                end_time = datetime.now() + timedelta(minutes=delay)
                self._update_task(
                    task.get("task_id"),
                    task_start_time,
                    task_end_time,
                    result
                )
            else:
                continue

    def image_register(self, deploy_params):
        """注册镜像"""
        url = f'{self.server_url}/image'
        return requests.post(url, json={
                "deploy_params": deploy_params,
                "service_code": self.service_code,
                "platform_code": self.platform_code
            }, timeout=10
        )
