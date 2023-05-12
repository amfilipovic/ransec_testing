import numpy as np
import matplotlib.pyplot
import matplotlib.pyplot as plt
import scipy as sp

# Set the x-axis limits to '0' and '100'.
plt.xlim(0, 100)
# Set the y-axis limits to '0' and '100'.
plt.ylim(0, 100)

# Load data from a CSV file using NumPy's 'loadtxt' function and set delimiter as comma.
data1 = np.loadtxt(fname='random_function_tester_cli1.csv', delimiter=',')
data2 = np.loadtxt(fname='random_function_tester_cli2.csv', delimiter=',')
data3 = np.loadtxt(fname='random_function_tester_cli3.csv', delimiter=',')
data4 = np.loadtxt(fname='random_function_tester_cli4.csv', delimiter=',')
data5 = np.loadtxt(fname='random_function_tester_cli5.csv', delimiter=',')

# Create a new Matplotlib figure with size 768x1024 px.
figure = matplotlib.pyplot.figure(figsize=(7.68, 10.24))

# Add 20 overlapping subplots to the figure in a 4x1 grid layout and store them in separate variables.
axes1_data = figure.add_subplot(4, 1, 1)
axes2_data = figure.add_subplot(4, 1, 2)
axes3_data = figure.add_subplot(4, 1, 3)
axes4_data = figure.add_subplot(4, 1, 4)

# Set y-axis label for first subplot to 'variance', rotate the label by 90 degrees, and plot the variance of each column of the data.
# The variance of a data set measures how far the values in the data set are from the mean.
# It is calculated as the average of the squared differences from the mean.
axes1_data.set_ylabel('variance', labelpad=0, rotation=90)
axes1_data.plot(data1.var(axis=0), color='blue')
axes1_data.plot(data2.var(axis=0), color='green')
axes1_data.plot(data3.var(axis=0), color='red')
axes1_data.plot(data4.var(axis=0), color='cyan')
axes1_data.plot(data5.var(axis=0), color='magenta')

# Set y-axis label for second subplot to 'mode', rotate the label by 90 degrees, and plot the mode of each column of the data.
# The mode of a data set is the value that appears most frequently in the data set.
axes2_data.set_ylabel('mode', labelpad=0, rotation=90)
axes2_data.plot(sp.stats.mode(data1, axis=0, keepdims=False)[0], color='blue')
axes2_data.plot(sp.stats.mode(data2, axis=0, keepdims=False)[0], color='green')
axes2_data.plot(sp.stats.mode(data3, axis=0, keepdims=False)[0], color='red')
axes2_data.plot(sp.stats.mode(data4, axis=0, keepdims=False)[0], color='cyan')
axes2_data.plot(sp.stats.mode(data5, axis=0, keepdims=False)[0], color='magenta')

# Set y-axis label for third subplot to 'skewness', rotate the label by 90 degrees, and plot the skewness of each column of the data.
# The skewness of a data set measures the degree of asymmetry of the data set. Positive skewness indicates a longer tail on the right side of the distribution, while negative skewness indicates a longer tail on the left side.
# It can be calculated using different formulas, but a common one is to use the third standardized moment, which is the expected value of the third power of the standardized deviations from the mean.
axes3_data.set_ylabel('skewness', labelpad=0, rotation=90)
axes3_data.plot(sp.stats.skew(data1), color='blue')
axes3_data.plot(sp.stats.skew(data2), color='green')
axes3_data.plot(sp.stats.skew(data3), color='red')
axes3_data.plot(sp.stats.skew(data4), color='cyan')
axes3_data.plot(sp.stats.skew(data5), color='magenta')

# Set y-axis label for fourth subplot to 'kurtosis', rotate the label by 90 degrees, and plot the kurtosis of each column of the data.
# The kurtosis of a data set measures the degree of peakedness of the data set. High kurtosis indicates a sharp peak, while low kurtosis indicates a flat distribution.
# It can be calculated using different formulas, but a common one is to use the fourth standardized moment, which is the expected value of the fourth power of the standardized deviations from the mean.
axes4_data.set_ylabel('kurtosis', labelpad=0, rotation=90)
axes4_data.plot(sp.stats.kurtosis(data1), color='blue')
axes4_data.plot(sp.stats.kurtosis(data2), color='green')
axes4_data.plot(sp.stats.kurtosis(data3), color='red')
axes4_data.plot(sp.stats.kurtosis(data4), color='cyan')
axes4_data.plot(sp.stats.kurtosis(data5), color='magenta')

# Align y-axis labels to the left.
axes1_data.yaxis.set_label_coords(-0.1, 0.5)
axes2_data.yaxis.set_label_coords(-0.1, 0.5)
axes3_data.yaxis.set_label_coords(-0.1, 0.5)
axes4_data.yaxis.set_label_coords(-0.1, 0.5)

# Adjust the subplots' layout to fit the contents of each subplot and avoid overlapping.
figure.tight_layout()

# Save the figure as a PNG file named 'random_function_tester_advsta_x5_cli.png'.
matplotlib.pyplot.savefig("random_function_tester_plot_advsta_x5_cli.png")