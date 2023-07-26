import matplotlib.pyplot as plt
import numpy as np

# 准备数据
x = np.linspace(-5, 5, 100)
y = x**2
# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(-5, 5), xticks=np.arange(-5, 5),
       ylim=(0, 25), yticks=np.arange(0, 25))

plt.show()
