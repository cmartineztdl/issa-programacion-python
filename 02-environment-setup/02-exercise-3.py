# 02-exercise-3
# 1. Open the “base_code.py” file and run it to get a working base code. Pay
# attention to:
#   - How to open a file.
#   - How to go through each line of the file.
#   - How to convert a string into a number.
# 2. Extend the base code to get the total sum of revenue.
# 3. Extend your code to get the percentage of revenue vs income.

import csv


def string_to_float(v):
    try:
        v = v.replace(',', '')
        return float(v)
    except Exception:
        return 0


# Open the data file
input_file = open('datasets/museums.csv', encoding='utf-8')
# Create a "reader" to go through the data
input_reader = csv.DictReader(input_file)

total_revenue = 0
total_income = 0

for line_data in input_reader:  # Loop to go through the data
    revenue = string_to_float(line_data['Revenue'])
    income = string_to_float(line_data['Income'])
    total_revenue = total_revenue + revenue
    total_income = total_income + income

print("Total revenue:", total_revenue)
print("Total income:", total_income)

revenue_percentage = (total_revenue / total_income) * 100
print("Revenue percentage: " + str(revenue_percentage) + "%")
