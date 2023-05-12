import csv
import random
from openpyxl import Workbook

# Define a function to generate random numbers (using 'random' module) according to specified parameters (number of random numbers to generate, number of generation rounds to do, and lower and upper range of numbers to generate).
def randomly_generate_numbers(number_of_numbers, number_of_rounds, lower_range, upper_range):
    list_of_generated_numbers = []
    for i in range(number_of_numbers):
        numbers = []
        for j in range(number_of_rounds):
            numbers.append(random.randint(lower_range, upper_range))
        list_of_generated_numbers.append(numbers)
    return list_of_generated_numbers

# Define a function to export data to Excel file.
def export2excel(data, filename):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "random"
    for i in range(len(data)):
        for j in range(len(data[i])):
            worksheet.cell(row=i+1, column=j+1, value=data[i][j])
    workbook.save(filename)

# Define a function to export data to CSV (Comma Separated Values) file.
def export2csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data)

# Define a function to export data to TSV (Tab Separated Values) file.
def export2tsv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(data)

# Define the number generating parameters (i.e. 10 numbers, 10 rounds in range from 0 to 100).
data = randomly_generate_numbers(10, 10, 0, 100)

# Define a function to regenerate random numbers according to specified parameters.
def generate_data(data):
    data = randomly_generate_numbers(10, 10, 0, 100)
    return data

# Example usage of the export2excel function.
export2excel(data, 'random_function_tester_cli.xlsx')

# Example usage of the export2csv function.
export2csv(data, 'random_function_tester_cli.csv')

# Example usage of the export2tsv function.
export2tsv(data, 'random_function_tester_cli.tsv')

"""
# Example multiple usage of the export2csv function.
# Loop 5 times.
for i in range(5):
    # Regenerate data for each iteration.
    data = generate_data(data)
    # Generate output name with unique numeric identifier.
    output_name = f'random_function_tester_cli{i+1}.csv'
    # Export data to CSV file with unique file name.
    export2csv(data, output_name)
"""