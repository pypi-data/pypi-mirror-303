import base64
import datetime
import hashlib
import hmac
import json
from urllib.parse import urlparse
import ssl
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time

import websocket


class Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, gpt_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.host = urlparse(gpt_url).netloc
        self.path = urlparse(gpt_url).path
        self.gpt_url = gpt_url

    # 生成url
    def create_url(self):
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"

        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()

        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'

        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        # 拼接鉴权参数，生成url
        url = self.gpt_url + '?' + urlencode(v)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        return url


# 收到websocket消息的处理
def on_message(message):
    # print(message)
    data = json.loads(message)
    code = data['header']['code']
    if code != 0:
        print(f'请求错误: {code}, {data}')
        return False, ""

    else:
        choices = data["payload"]["choices"]
        status = choices["status"]
        content = choices["text"][0]["content"]
        if status == 2:
            print("#### 关闭会话")
            return False, ""
        else:
            print(content, end='')
            return True, content


def gen_params(appid, query, domain):
    """
    通过appid和用户的提问来生成请参数
    """

    data = {
        "header": {
            "app_id": appid,
            "uid": "1234",
            # "patch_id": []    #接入微调模型，对应服务发布后的resourceid
        },
        "parameter": {
            "chat": {
                "__domain": domain,
                "temperature": 0.5,
                "max_tokens": 4096,
                "auditing": "default",
            }
        },
        "payload": {
            "message": {
                "text": [{"role": "user", "content": query}]
            }
        }
    }
    return data


def main(appid, api_secret, api_key, gpt_url, domain, query):
    wsParam = Ws_Param(appid, api_key, api_secret, gpt_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    #
    ws = websocket.create_connection(wsUrl, sslopt={"cert_reqs": ssl.CERT_NONE})
    # 发送请求
    data = json.dumps(gen_params(appid=appid, query=query, domain=domain))
    ws.send(data)
    # 接受请求
    完整响应内容 = ""
    while True:
        response = ws.recv()
        isOK, content = on_message(response)
        完整响应内容 += content
        if isOK is False:
            break
    #
    ws.close()
    #
    return 完整响应内容


if __name__ == "__main__":
    from ai_tools_zxw.LLM_API.LLM_ifly.api.config import appid, api_key, api_secret, self_model_ws_url, self_model_serviceId

    # 私有模型，今日已用：182
    main(
        appid=appid,
        api_secret=api_key,
        api_key=api_secret,
        gpt_url=self_model_ws_url,
        domain=self_model_serviceId,
        query="帮我写一篇情书"
    )
