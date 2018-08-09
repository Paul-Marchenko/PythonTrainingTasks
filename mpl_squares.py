import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
#from matplotlib.backends import _macosx

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.plot(squares)
plt.show()