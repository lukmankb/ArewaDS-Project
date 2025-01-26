from random import randint
class Die:
    """A class representing a single die"""
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1, self.num_sides)
import plotly.express as px
from rolling_die import Die
# crete D6
die = Die() 
die_2 = Die(10)
results = []
for roll_num in range(50_000):
    result = die.roll() + die_2.roll()
    results.append(result)
frequencies = []
max_result = die.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)
# Visualize the results.
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick=1)
#fig.show()
#fig.write_html('dice_visual_d6d10.html')
# TRY IT YOURSELF
'''
15-6. Two D8s: Create a simulation showing what happens when you roll two eight-sided dice 1,000 times. Try to picture what you think the visualization will look like before you run the simulation, then see if your intuition was correct. Gradually increase the number of rolls until you start to see the limits of your system’s capabilities.
15-7.  Three Dice: When you roll three D6 dice, the smallest number you can roll is 3 and the largest number is 18. Create a visualization that shows what hap-pens when you roll three D6 dice.
15-8. Multiplication: When you roll two dice, you usually add the two numbers together to get the result. Create a visualization that shows what happens if you multiply these numbers by each other instead.
15-9.  Die Comprehensions: For clarity, the listings in this section use the long form of for loops. If you’re comfortable using list comprehensions, try writing a comprehension for one or both of the loops in each of these programs.
15-10. Practicing with Both Libraries: Try using Matplotlib to make a die-rolling visualization, and use Plotly to make the visualization for a random walk. (You’ll need to consult the documentation for each library to complete this exercise.)
'''
#15-6. Two D8s: Create a simulation showing what happens when you roll two eight-sided dice 1,000 times. Try to picture what you think the visualization will look like before you run the simulation, then see if your intuition was correct. Gradually increase the number of rolls until you start to see the limits of your system’s capabilities.
die = Die(8)
die_2 = Die(8)
results = []
for roll_num in range(1_000):
    result = die.roll() + die_2.roll()
    results.append(result)
frequencies = []
max_result = die.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)
# Visualize the results.
title = "Results of Rolling Two D8 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

#15-7.  Three Dice: When you roll three D6 dice, the smallest number you can roll is 3 and the largest number is 18. Create a visualization that shows what hap-pens when you roll three D6 dice.
die = Die()
die_2 = Die()
die_3 = Die()
results = []
for roll_num in range(1_000):
    result = die.roll() + die_2.roll() + die_3.roll()
    results.append(result)
frequencies = []
max_result = die.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)
# Visualize the results.
title = "Results of Rolling Three D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

#15-8. Multiplication: When you roll two dice, you usually add the two numbers together to get the result. Create a visualization that shows what happens if you multiply these numbers by each other instead.
die = Die()
die_2 = Die()
results = []
for roll_num in range(1_000):
    result = die.roll() * die_2.roll()
    results.append(result)
frequencies = []
max_result = die.num_sides * die_2.num_sides
poss_results = range(1, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)
# Visualize the results.
title = "Results of Multiplying Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

#15-9.  Die Comprehensions: For clarity, the listings in this section use the long form of for loops. If you’re comfortable using list comprehensions, try writing a comprehension for one or both of the loops in each of these programs.
die = Die()
die_2 = Die()
results = [die.roll() * die_2.roll() for roll_num in range(1_000)]
frequencies = []
max_result = die.num_sides * die_2.num_sides
poss_results = range(1, max_result+1)
frequencies = [results.count(value) for value in poss_results]
#print(frequencies)
# Visualize the results.
title = "Results of Multiplying Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

#15-10. Practicing with Both Libraries: Try using Matplotlib to make a die-rolling visualization, and use Plotly to make the visualization for a random walk. (You’ll need to consult the documentation for each library to complete this exercise.)
import matplotlib.pyplot as plt
die = Die()
die_2 = Die()
results = [die.roll() * die_2.roll() for roll_num in range(1_000)]
frequencies = []
max_result = die.num_sides * die_2.num_sides
poss_results = range(1, max_result+1)
frequencies = [results.count(value) for value in poss_results]
#print(frequencies)
# Visualize the results.
title = "Results of Multiplying Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

