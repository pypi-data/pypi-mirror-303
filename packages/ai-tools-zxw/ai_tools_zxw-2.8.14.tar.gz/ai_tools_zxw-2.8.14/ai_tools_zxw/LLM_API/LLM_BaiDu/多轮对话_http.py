"""
# File       : 试试_LLM异步.py
# Time       ：2024/9/15 下午7:39
# Author     ：xuewei zhang
# Email      ：shuiheyangguang@gmail.com
# version    ：python 3.12
# Description：
"""
"""
pip install qianfan # 闻心一言 大模型
"""
import os
from typing import List
import qianfan
from ai_tools_zxw.LLM_API import LLM
from ai_tools_zxw.LLM_API.config import BAIDU
from enum import Enum


class LLM_Model(str, Enum):
    ernie4 = "ERNIE-4.0-8K-Latest"  # 输入：¥0.04元/千tokens；输出：¥0.12元/千tokens
    ernie35_0701 = "ERNIE-3.5-8K-0701"  # 输入：¥0.004元/千tokens ； 输出：¥0.012元/千tokens
    ernie35_0613 = "ERNIE-3.5-8K-0613"  # ¥0.004元/千tokens


class ChatToLLM(LLM):
    chat_history = [
        # {"role": "system", "content": "你现在扮演李白，你豪情万丈，狂放不羁；接下来请用李白的口吻和用户对话。"} , # 设置对话背景或者模型角色
        # {"role": "user", "content": "你是谁"},  # 用户的历史问题
        # {"role": "assistant", "content": "....."} , # AI的历史回答结果
        # # ....... 省略的历史对话
        # {"role": "user", "content": "你会做什么"}  # 最新的一条问题，如无需上下文，可只传最新一条问题
    ]

    usage_statistic = [
        # {'prompt_tokens': 6, 'completion_tokens': 348, 'total_tokens': 354},
    ]

    def __init__(self,
                 access_key: str = BAIDU.access_key,
                 secret_key: str = BAIDU.secret_key,
                 model: LLM_Model = LLM_Model.ernie4):
        self.model = model.value

        os.environ["QIANFAN_ACCESS_KEY"] = access_key
        os.environ["QIANFAN_SECRET_KEY"] = secret_key

        self.client = qianfan.ChatCompletion()

    def __del__(self):
        del self.client

    def chat(self, input_content: str, single_chat=False) -> str:
        """
        resp["body"] 值示例：
        {
            "id: "xxx",
            "object": "chat.completion",
            "created": 1719051799,
            "result": "xxx",
            "is_truncated": false,
            "need_clear_history": false,
            "finish_response": 'normal',
            'usage': {'prompt_tokens': 0, 'completion_tokens': 0, 'total_tokens': 0}
        }
        :param input_content:
        :param single_chat: 是否为单次对话
        :return:
        """
        # 1. 设置聊天记录
        chat_history = self._check_length(self._set_text("user", input_content))
        if single_chat is True:
            chat_history = chat_history[-1:]
            # print("采用单次对话模式: ", len(chat_history))

        # 2. 对话
        resp = self.client.do(
            model=self.model,  # 指定请求的版本
            messages=chat_history
        )
        # 3. 设置聊天记录
        res = self._set_text("assistant", resp["body"]["result"])
        self._set_usage(resp["body"]["usage"])

        return res[-1]["content"]

    async def chat_async(self, input_content: str, single_chat=False) -> str:
        """
        resp["body"] 值示例：
        {
            "id: "xxx",
            "object": "chat.completion",
            "created": 1719051799,
            "result": "xxx",
            "is_truncated": false,
            "need_clear_history": false,
            "finish_response": 'normal',
            'usage': {'prompt_tokens': 0, 'completion_tokens': 0, 'total_tokens': 0}
        }
        :param input_content:
        :param single_chat: 是否为单次对话
        :return:
        """
        # 1. 设置聊天记录
        chat_history = self._check_length(self._set_text("user", input_content))
        if single_chat is True:
            chat_history = chat_history[-1:]
            # print("采用单次对话模式: ", len(chat_history))

        # 2. 对话
        resp = await self.client.ado(
            model=self.model,  # 指定请求的版本
            messages=chat_history
        )
        # 3. 设置聊天记录
        res = self._set_text("assistant", resp["body"]["result"])
        self._set_usage(resp["body"]["usage"])

        return res[-1]["content"]

    def 添加上下文(self, role, content):
        """
        :param role: system, user, assistant
        :param content:
        :return:
        """
        self._set_text(role, content)

    def 清除所有上下文(self):
        self.chat_history = []

    def 删除上条对话(self):
        last = self.chat_history[:-1]
        if len(last) % 2 != 0:
            last = last[:-1]
        self.chat_history = last

    def _set_usage(self, usage: dict):
        self.usage_statistic.append(usage)
        return self.usage_statistic

    def _set_text(self, role, content) -> List[dict]:
        json_con = {"role": role, "content": content}
        self.chat_history.append(json_con)
        return self.chat_history

    def _check_length(self, text):
        while self.__get_length(text) > 18000:
            del text[0]

        # check if the beginning is not user
        if text[0]["role"] != "user":
            del text[0]

        return text

    @staticmethod
    def __get_length(text: List[dict]):
        length = 0
        for content in text:
            temp = content["content"]
            leng = len(temp)
            length += leng
        return length


if __name__ == '__main__':
    from config import LLM_BAIDU
    from asyncio import run

    # General
    get_response = ChatToLLM(LLM_BAIDU.access_key, LLM_BAIDU.secret_key, LLM_Model.ernie35_0701)
    a = run(get_response.chat_async("请帮我写一份情书", single_chat=True))
    print(a)
    print(get_response.usage_statistic)

    # selfLLM - 无效
    # selfLLM = GetLLMResponse(model="xscnllama2")
    # b = selfLLM.get("你的基础模型是什么？")
    # print(b)
