# coding: utf-8
from typing import List
from ai_tools_zxw.LLM_API.LLM_ifly.api.General.chat.__SparkApi import SparkAPI
from ai_tools_zxw.LLM_API.config import ifly_appid, ifly_api_key, ifly_secret_key


class ChatAPI:
    __domain = "generalv3.5"  # Max版本
    # __domain = "generalv3"       # Pro版本
    # __domain = "general"         # Lite版本

    __Spark_url = "wss://spark-api.xf-yun.com/v3.5/chat"  # Max服务地址
    # __Spark_url = "wss://spark-api.xf-yun.com/v3.1/chat"  # Pro服务地址
    # __Spark_url = "wss://spark-api.xf-yun.com/v1.1/chat"  # Lite服务地址

    # 初始上下文内容，当前可传system、user、assistant 等角色
    chat_history = [
        # {"role": "system", "content": "你现在扮演李白，你豪情万丈，狂放不羁；接下来请用李白的口吻和用户对话。"} , # 设置对话背景或者模型角色
        # {"role": "user", "content": "你是谁"},  # 用户的历史问题
        # {"role": "assistant", "content": "....."} , # AI的历史回答结果
        # # ....... 省略的历史对话
        # {"role": "user", "content": "你会做什么"}  # 最新的一条问题，如无需上下文，可只传最新一条问题
    ]

    def __init__(self):
        self.__spark_api = SparkAPI()

    def chat(self, my_input: str) -> str:
        # 1.整理好的对话内容，翻译成英文：The arranged conversation content
        my_input_organized = self._check_length(self._set_text("user", my_input))
        # 2.请求星火接口：Request Spark API
        self.__spark_api.answer = ""
        self.__spark_api.main(ifly_appid, ifly_api_key, ifly_secret_key, self.__Spark_url, self.__domain, my_input_organized)
        # 3.将答案存入对话：put the answer into the chat box
        self._set_text("assistant", self.__spark_api.answer)
        # 4.返回答案：return the answer
        return self.__spark_api.answer

    def 添加上下文(self, role, content):
        """
        :param role: system, user, assistant
        :param content:
        :return:
        """
        self._set_text(role, content)

    def 清除所有上下文(self):
        self.chat_history = []

    def _set_text(self, role, content) -> List[dict]:
        json_con = {"role": role, "content": content}
        self.chat_history.append(json_con)
        return self.chat_history

    @staticmethod
    def _get_length(text: List[dict]):
        length = 0
        for content in text:
            temp = content["content"]
            leng = len(temp)
            length += leng
        return length

    def _check_length(self, text):
        while self._get_length(text) > 8000:
            del text[0]
        return text


if __name__ == '__main__':
    chat = ChatAPI()
    while True:
        Input = input("\n" + "我:")
        print("星火:", end="")
        answer = chat.chat(Input)
