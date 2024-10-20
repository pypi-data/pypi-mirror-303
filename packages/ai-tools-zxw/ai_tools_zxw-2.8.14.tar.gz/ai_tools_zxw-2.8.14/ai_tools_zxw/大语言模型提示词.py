"""
# File       : 大语言模型提示词.py
# Time       ：2024/7/21 上午8:23
# Author     ：
# Email      ：
# version    ：python 3.12
# Description：生成提示词
"""

prompt = {
    "context": "这是一个大语言模型的训练数据集，每条数据之间使用换行符分隔。每条数据包含以下字段：输入内容、输出内容。",
    "objective": "你需要完成的任务是：清洗每条数据，去除无效字符。",
    "audience": "你的受众是：大语言模型训练集",
    "response": "你输出的格式与输入的格式一致，每条数据之间使用换行符分隔。",
    "training_data": "训练数据：\n\n输入内容\t输出内容\n\n这是一个训练数据\t\r这是一个的训练数据"
}


def train_txt_文本清洗(training_data: str):
    res = f"""#CONTEXT(上下文)#
{prompt['context']}
#OBJECTIVE(目标)#
{prompt['objective']}
#AUDIENCE(观众)#
{prompt['audience']}
#RESPONSE(回答)#
{prompt['response']}
#TRAINING_DATA(训练数据)#
{training_data}"""
    return res


class set_prompt:
    def __init__(self,
                 上下文,
                 目标,
                 风格="以行业专家的风格",
                 语气="以正式的语气",
                 受众="你的受众是：行业新人",
                 响应="只输出‘是’或‘否’"):
        self.context = 上下文
        self.objective = 目标
        self.style = 风格
        self.tone = 语气
        self.audience = 受众
        self.response = 响应

    def prompt_to_input(self):
        res = f"""#CONTEXT(上下文)#
{self.context}
#OBJECTIVE(目标)#
{self.objective}
#STYLE(风格)#
{self.style}
#TONE(语气)#
{self.tone}
#AUDIENCE(观众)#
{self.audience}
#RESPONSE(回答)#
{self.response}
        """
        return res
