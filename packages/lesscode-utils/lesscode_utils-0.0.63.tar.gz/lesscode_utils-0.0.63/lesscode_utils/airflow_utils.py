import datetime

from lesscode_utils.request import get_basic_auth, sync_common_post


class AirflowUtil:
    def __init__(self, url, username, password):
        self.auth = get_basic_auth(username, password) if username and password else None
        self.url = url

    def run(self, conf):
        headers = {
            'content-type': 'application/json'
        }
        data = {
            "execution_date": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f+08:00"),
            "conf": conf
        }
        res = sync_common_post(self.url, json=data, result_type="origin", headers=headers, auth=self.auth)
        return res
