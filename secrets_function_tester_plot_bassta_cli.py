import numpy as np
import matplotlib.pyplot
import matplotlib.pyplot as plt

# Set the x-axis limits to '0' and '100'.
plt.xlim(0, 100)
# Set the y-axis limits to '0' and '100'.
plt.ylim(0, 100)

# Load data from a CSV file using NumPy's 'loadtxt' function and set delimiter as comma.
data = np.loadtxt(fname='secrets_function_tester_cli.csv', delimiter=',')

# Create a new Matplotlib figure with size 768x1024 px.
figure = matplotlib.pyplot.figure(figsize=(7.68, 10.24))

# Add 4 subplots to the figure in a 4x1 grid layout and store them in separate variables.
axes1 = figure.add_subplot(4, 1, 1)
axes2 = figure.add_subplot(4, 1, 2)
axes3 = figure.add_subplot(4, 1, 3)
axes4 = figure.add_subplot(4, 1, 4)

# Set y-axis label for first subplot to 'average', rotate the label by 90 degrees, and plot the mean of each column of the data.
# The average (mean) of a data set represents the central tendency of the data set.
# It is calculated by adding up all the values in the data set and dividing the sum by the total number of values.
axes1.set_ylabel('average', labelpad=0, rotation=90)
axes1.plot(data.mean(axis=0))

# Set y-axis label for second subplot to 'maximum', rotate the label by 90 degrees, and plot the maximum of each column of the data.
# The maximum of a data set is the largest value in the set, i.e., the value that is greater than or equal to all the other values in the set.
axes2.set_ylabel('maximum', labelpad=0, rotation=90)
axes2.plot(data.max(axis=0))

# Set y-axis label for third subplot to 'minimum', rotate the label by 90 degrees, and plot the minimum of each column of the data.
# The minimum of a data set is the smallest value in the set, i.e., the value that is less than or equal to all the other values in the set.
axes3.set_ylabel('minimum', labelpad=0, rotation=90)
axes3.plot(data.min(axis=0))

# Set y-axis label for fourth subplot to 'standard deviation', rotate the label by 90 degrees, and plot the standard deviation of each column of the data.
# The standard deviation of a data set is a measure of how spread out the data is from the mean (how much it deviates from the average value).
# It is calculated by taking the square root of the average of the squared differences of each value from the mean.
axes4.set_ylabel('standard deviation', labelpad=0, rotation=90)
axes4.plot(data.std(axis=0))

# Align y-axis labels to the left.
axes1.yaxis.set_label_coords(-0.1, 0.5)
axes2.yaxis.set_label_coords(-0.1, 0.5)
axes3.yaxis.set_label_coords(-0.1, 0.5)
axes4.yaxis.set_label_coords(-0.1, 0.5)

# Adjust the subplots' layout to fit the contents of each subplot and avoid overlapping.
figure.tight_layout()

# Save the figure as a PNG file named 'random_function_tester_bassta_cli.png'.
matplotlib.pyplot.savefig("secrets_function_tester_plot_bassta_cli.png")