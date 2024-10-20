"""
pip install scikit-learn numpy pandas matplotlib
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 生成示例数据
np.random.seed(42)
x = np.random.rand(100, 2)

# 创建KMeans模型并拟合数据
n_clusters = 3  # 设置聚类的数量
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(x)

# 获取聚类结果
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 将数据保存到Pandas数据框中
data = pd.DataFrame({
    'x1': x[:, 0],
    'x2': x[:, 1],
    'label': labels
})

# 打印数据框
print(data)

# 绘制聚类结果
plt.figure(figsize=(10, 6))
colors = ['blue', 'green', 'red']

for i in range(n_clusters):
    cluster = data[data['label'] == i]
    plt.scatter(cluster['x1'], cluster['x2'], color=colors[i], label=f'Cluster {i + 1}')

# 绘制聚类中心
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='yellow', marker='*', label='Centroids')

# 添加标题和标签
plt.title('KMeans Clustering')
plt.xlabel('X1')
plt.ylabel('X2')
plt.legend()

# 显示图形
plt.show()
