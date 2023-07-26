# Matplotlib

## 1.导入包
```python
import matplotlib.pyplot as plt
import numpy as np
```

## 2.准备数据
使用 Numpy 生成 X Y 数据  
```python
x = np.linspace(-5, 5, 100)
y = x**2
```

## 3.创建图表
```python
fig, ax = plt.subplots()
```

## 4.绘制数据
```python
# 线条图
ax.plot()
# 散点图
ax.scatter()
........
```

## 5.设置轴对象属性
```python
ax.set(xlim=(-5, 5), xticks=np.arange(-5, 5),
       ylim=(0, 25), yticks=np.arange(0, 25))
```

## 6.展示图表
```python
plt.show()
```