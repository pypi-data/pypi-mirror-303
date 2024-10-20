import matplotlib.pyplot as plt

# 示例数据
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [23, 17, 35, 29]

# 创建柱状图
plt.figure(figsize=(10, 6))  # 10x6 inches
bars = plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])

# 添加标题和标签
plt.title('Example Bar Chart', fontsize=16)
plt.xlabel('Categories', fontsize=14)
plt.ylabel('Values', fontsize=14)

# 在每个柱状图顶部添加数值标签
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, round(yval, 2), ha='center', va='bottom', fontsize=12)

# 显示图形
plt.show()
