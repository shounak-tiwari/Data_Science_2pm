import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [60,89,75,98]

plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.title("Simple line plot")
plt.savefig('lineplot.png')
plt.show()