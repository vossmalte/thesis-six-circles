import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("pgf")

c_1 = 2
c_2 = 1.5

dt = 0.01
t_1 = np.arange(0, c_1-c_2, dt)
t_2 = np.arange(c_1-c_2, c_1, dt)
t_3 = np.arange(c_1, c_1+c_2, dt)
t_4 = np.arange(c_1+c_2, 5, dt)

y_1 = c_1-c_2-t_1
y_2 = t_2-(c_1-c_2)
y_3 = c_1+c_2-t_3
y_4 = t_4-(c_1+c_2)

# fig, ax = plt.plot()
plt.plot(t_1, y_1, t_2, y_2, t_3, y_3, t_4, y_4)
# TODO: beautify this graph
# show ticks at c_i-c_i....
# show y-ticks at c_2
# remove numbers

# plt.show()
plt.savefig("figures/f_in_parallelogram.pgf")
