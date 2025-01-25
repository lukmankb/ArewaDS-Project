'''
Cubes:  A number raised to the third power is a cube. Plot the first five cubic numbers.
15-2. Colored Cubes: Apply a colormap to your cubes plot.
'''
import matplotlib.pyplot as plt
x_values = range(1, 6)
y_values = [x**3 for x in x_values]
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=100) #Apply colormap to the plot
# Set chart title and label axes.
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(labelsize=14)
plt.savefig('first_five_cubic_numbers.png', bbox_inches='tight') # save as file
plt.show()
