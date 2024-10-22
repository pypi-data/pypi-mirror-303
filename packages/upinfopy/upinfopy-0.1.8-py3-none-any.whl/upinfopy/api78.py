import requests
import sys
import os
# 将包目录添加到模块搜索路径中
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from upinfo import UpInfo

class Api78:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_request(self, endpoint, params):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # 检查响应状态码
            return response.json()  # 返回JSON格式的数据
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

# 示例使用
if __name__ == "__main__":
    
    up= UpInfo()
    up.sid="GUEST888-8888-8888-8888-GUEST88GUEST"
    up.uname="guest"
    UpInfo.setMaster(up)

    up.set_par("gameid", 42)
    sendtext=up.to_url_encode()
    
    client = Api78("http://test.778878.net")
    params = sendtext
    result = client.send_request("apitest/testmenu/testtb/get", params)
    print(result)
        