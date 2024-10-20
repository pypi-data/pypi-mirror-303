import matplotlib.pyplot as plt

# 示例数据
x = range(10)
y1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y3 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 创建折线图
plt.plot(x, y1, label='Line 1', color='blue')
#
plt.plot(x, y2, label='Line 2', color='green')
#
plt.plot(x, y3, label='Line 3', color='red')
plt.scatter(x, y3, color='red')

# 添加图例
plt.legend()

# 添加标题和标签
plt.title('Multiple Lines with Different Colors')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示图形
plt.show()
