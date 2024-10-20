def remove_invalid_utf8(text):
    # 尝试将字符串编码为UTF-8字节并解码，忽略错误
    cleaned_text = text.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
    return cleaned_text


# 示例文本，包含一些无效的UTF-8字符
sample_text = "这是一个示例文本，包含无效字符\x80\x80和一些表情😊。This is a test."

# 去除无效的UTF-8字符
cleaned_text = remove_invalid_utf8(sample_text)

# 输出结果
print("原始文本：", sample_text)
print("清理后的文本：", cleaned_text)
