import matplotlib.pyplot as plt

valores_x = range(13)

valores_y = [x*x for x in valores_x]

plt.plot(valores_x, valores_y)
plt.xlabel("x")
plt.ylabel("x^2")
plt.show()