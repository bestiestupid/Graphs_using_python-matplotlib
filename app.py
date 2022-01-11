import matplotlib.pyplot as pl

x = [1, 2, 3, 4]
y = [1000, 1500, 1800,  2500]
legend_x = ["Joe", "John", "Rose", "Paul"]
pl.xticks(x, legend_x)
pl.plot(x, y)
pl.show()
