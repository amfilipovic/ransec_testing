import numpy as np
import matplotlib.pyplot
import matplotlib.pyplot as plt

# Set the x-axis limits to '0' and '100'.
plt.xlim(0, 100)
# Set the y-axis limits to '0' and '100'.
plt.ylim(0, 100)

# Load data from a CSV file using NumPy's 'loadtxt' function and set delimiter as comma.
data1 = np.loadtxt(fname='secrets_function_tester_cli1.csv', delimiter=',')
data2 = np.loadtxt(fname='secrets_function_tester_cli2.csv', delimiter=',')
data3 = np.loadtxt(fname='secrets_function_tester_cli3.csv', delimiter=',')
data4 = np.loadtxt(fname='secrets_function_tester_cli4.csv', delimiter=',')
data5 = np.loadtxt(fname='secrets_function_tester_cli5.csv', delimiter=',')

# Create a new Matplotlib figure with size 768x1024 px.
figure = matplotlib.pyplot.figure(figsize=(7.68, 10.24))

# Add 20 overlapping subplots to the figure in a 4x1 grid layout and store them in separate variables.
axes1_data = figure.add_subplot(4, 1, 1)
axes2_data = figure.add_subplot(4, 1, 2)
axes3_data = figure.add_subplot(4, 1, 3)
axes4_data = figure.add_subplot(4, 1, 4)

# Set y-axis label for first subplot to 'average', rotate the label by 90 degrees, and plot the mean of each column of the data.
# The average (mean) of a data set represents the central tendency of the data set.
# It is calculated by adding up all the values in the data set and dividing the sum by the total number of values.
axes1_data.set_ylabel('average', labelpad=0, rotation=90)
axes1_data.plot(data1.mean(axis=0), color='blue')
axes1_data.plot(data2.mean(axis=0), color='green')
axes1_data.plot(data3.mean(axis=0), color='red')
axes1_data.plot(data4.mean(axis=0), color='cyan')
axes1_data.plot(data5.mean(axis=0), color='magenta')

# Set y-axis label for second subplot to 'maximum', rotate the label by 90 degrees, and plot the maximum of each column of the data.
# The maximum of a data set is the largest value in the set, i.e., the value that is greater than or equal to all the other values in the set.
axes2_data.set_ylabel('maximum', labelpad=0, rotation=90)
axes2_data.plot(data1.max(axis=0), color='blue')
axes2_data.plot(data2.max(axis=0), color='green')
axes2_data.plot(data3.max(axis=0), color='red')
axes2_data.plot(data4.max(axis=0), color='cyan')
axes2_data.plot(data5.max(axis=0), color='magenta')

# Set y-axis label for third subplot to 'minimum', rotate the label by 90 degrees, and plot the minimum of each column of the data.
# The minimum of a data set is the smallest value in the set, i.e., the value that is less than or equal to all the other values in the set.
axes3_data.set_ylabel('minimum', labelpad=0, rotation=90)
axes3_data.plot(data1.min(axis=0), color='blue')
axes3_data.plot(data2.min(axis=0), color='green')
axes3_data.plot(data3.min(axis=0), color='red')
axes3_data.plot(data4.min(axis=0), color='cyan')
axes3_data.plot(data5.min(axis=0), color='magenta')

# Set y-axis label for fourth subplot to 'standard deviation', rotate the label by 90 degrees, and plot the standard deviation of each column of the data.
# The standard deviation of a data set is a measure of how spread out the data is from the mean (how much it deviates from the average value).
# It is calculated by taking the square root of the average of the squared differences of each value from the mean.
axes4_data.set_ylabel('standard deviation', labelpad=0, rotation=90)
axes4_data.plot(data1.std(axis=0), color='blue')
axes4_data.plot(data2.std(axis=0), color='green')
axes4_data.plot(data3.std(axis=0), color='red')
axes4_data.plot(data4.std(axis=0), color='cyan')
axes4_data.plot(data5.std(axis=0), color='magenta')

# Align y-axis labels to the left.
axes1_data.yaxis.set_label_coords(-0.1, 0.5)
axes2_data.yaxis.set_label_coords(-0.1, 0.5)
axes3_data.yaxis.set_label_coords(-0.1, 0.5)
axes4_data.yaxis.set_label_coords(-0.1, 0.5)

# Adjust the subplots' layout to fit the contents of each subplot and avoid overlapping.
figure.tight_layout()

# Save the figure as a PNG file named 'secrets_function_tester_bassta_x5_cli.png'.
matplotlib.pyplot.savefig("secrets_function_tester_plot_bassta_x5_cli.png")