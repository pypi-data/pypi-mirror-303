"""
# File       : chat.py
# Time       ：2024/8/14 上午10:37
# Author     ：xuewei zhang
# Email      ：shuiheyangguang@gmail.com
# version    ：python 3.12
# Description：pip install anthropic
"""
import anthropic
from ai_tools_zxw.LLM_API.config import Cluade

client = anthropic.Anthropic(api_key=Cluade.api_key)


message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why is the ocean salty?"
                }
            ]
        }
    ]
)
print(message.content)
