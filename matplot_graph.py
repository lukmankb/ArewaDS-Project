import matplotlib.pyplot as plt
#input_values = [1,2,3,4,5]
#squares = [1, 4, 9, 16, 25]
#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#Set size of tick labels.
ax.tick_params(labelsize=14)
# set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])
#ax.ticklabel_format(style='plain')
plt.savefig('squares_plot.png', bbox_inches='tight') # save as file
plt.show()

# TRY IT YOURSELF:
'''
Cubes:  A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5,000 cubic numbers.
15-2. Colored Cubes: Apply a colormap to your cubes plot.
'''
# The exercises have been done in separate python files.