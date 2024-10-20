"""
pip install scikit-learn numpy pandas matplotlib
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# 示例数据
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([2.3, 2.1, 4.5, 3.8, 5.9, 7.3, 7.1, 8.8, 9.0, 9.8])

# 多项式特征变换
degree = 3  # 设置多项式的度数
poly = PolynomialFeatures(degree)
x_poly = poly.fit_transform(x)

# 线性回归模型拟合
model = LinearRegression()
model.fit(x_poly, y)

# 预测
y_pred = model.predict(x_poly)

# 将原始数据和拟合结果保存到Pandas数据框中
data = pd.DataFrame({
    'x': x.flatten(),
    'y': y,
    'y_pred': y_pred
})

# 打印数据框
print(data)

# 绘制原始数据点和拟合曲线
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_pred, color='red', label=f'Polynomial Fit (degree={degree})')
plt.title('Polynomial Fit Example using sklearn')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
