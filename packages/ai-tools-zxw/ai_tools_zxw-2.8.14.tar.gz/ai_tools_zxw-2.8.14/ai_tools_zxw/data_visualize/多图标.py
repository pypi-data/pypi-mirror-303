import matplotlib.pyplot as plt

# 创建一个包含四个子图的2x2网格
fig, axs = plt.subplots(2, 2, figsize=(12, 10))  # 12x10英寸

# 数据
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]
categories = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# 第一个宫格：散点图
axs[0, 0].scatter(x, y, color='blue')
axs[0, 0].set_title('Scatter Plot')
axs[0, 0].set_xlabel('X Axis')
axs[0, 0].set_ylabel('Y Axis')

# 第二个宫格：留空
axs[0, 1].axis('off')

# 第三个宫格：留空
axs[1, 0].axis('off')

# 第四个宫格：饼图
axs[1, 1].pie(sizes, labels=categories, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'purple'])  # autopct 显示百分比
axs[1, 1].set_title('Pie Chart')

# 设置布局
plt.tight_layout()

# 显示图形
plt.show()
