"""
pip install jieba emoji
"""
import re
import emoji
import jieba
from typing import List

# 示例停用词列表，可以根据需要扩展
stopwords = {"的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都",
             "一", "一个", "上", "也", "很", "到",
             "说", "要", "去", "你", "会", "着", "没有", "看", "好", "自己", "这"}


def preprocess_text(text):
    # 英文标点转中文标点
    punctuation_map = {
        ',': '，',
        '.': '。',
        '!': '！',
        '?': '？',
        ';': '；',
        ':': '：',
        '"': '“',
        "'": '‘',
        '(': '（',
        ')': '）',
        '[': '【',
        ']': '】',
        '{': '《',
        '}': '》',
    }
    for eng_punct, zh_punct in punctuation_map.items():
        text = text.replace(eng_punct, zh_punct)

    # 去除HTML标签
    text = re.sub(r'<.*?>', '', text)

    # 去除URL
    text = re.sub(r'http[s]?://\S+', '', text)

    # 去除表情符号
    text = emoji.replace_emoji(text, replace='')

    # 去除特殊字符和标点符号
    text = re.sub(r'[^\w\s\u4e00-\u9fff]', '', text)

    # 去除特殊字符，不包括标点符号
    ...

    # 去除多余的空格
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def remove_stopwords(words):
    # 去除停用词
    return [word for word in words if word not in stopwords]


def segment_and_clean(text):
    # 分词
    words = jieba.lcut(text)
    # 去除停用词
    clean_words = remove_stopwords(words)
    return clean_words


def recognize_chinese_character(text: str) -> List[str]:
    """
    中文字符大致位于 Unicode 范围 \u4e00-\u9fff。
    中文标点则分布在多个区间，包括但不限于：
        •	\u3000-\u303f：中文标点符号
        •	\uff00-\uffef：全角ASCII、全角标点
    """
    # 编译正则表达式以匹配中文字符和中文标点符号
    pattern = re.compile(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]+')

    # 使用findall方法找到所有匹配项
    matches = pattern.findall(text)
    return matches

def recognize_chinese_characters_exclude_punctuation(text: str) -> List[str]:
    """
    识别中文文字，不包括中文标点。
    中文字符大致位于 Unicode 范围 \u4e00-\u9fff。
    """
    # 编译正则表达式以仅匹配中文字符
    pattern = re.compile(r'[\u4e00-\u9fff]+')

    # 使用findall方法找到所有匹配项
    matches = pattern.findall(text)
    return matches



if __name__ == '__main__':
    # 示例文本
    sample_text = "你好，世界！这是一个测试：全角符号＋汉字++。这是一个示例文本，包含HTML标签<a href='https://example.com'>链接</a>、表情😊和特殊字符！@#￥%……&*（）。"

    # # 预处理文本
    # cleaned_text = preprocess_text(sample_text)
    # print("预处理后的文本：", cleaned_text)
    #
    # # 分词并去除停用词
    # clean_words = segment_and_clean(cleaned_text)
    # print("分词并去除停用词后的词语：", clean_words)

    # 识别中文字符
    x = recognize_chinese_character(sample_text)
    print(x)
