# 03-exercise-1
# Using the dataset “tripadvisor_museum_world.csv”, get the number of museums
# with a rating above 4.
# 1. “Plan” your code/algorithm.
# 2. Implement.
# 3. Validate the result: 836

import csv


def string_to_float(v):
    try:
        v = v.replace(',', '')
        return float(v)
    except Exception:
        return 0


# Open the data file
input_file = open('datasets/tripadvisor_museum_world.csv', encoding='utf-8')
# Create a "reader" to go through the data
input_reader = csv.DictReader(input_file)

# Init counter to count number of museums
number_of_museums = 0

for line_data in input_reader:  # Loop to go through the data
    # Get the rating value for the museum
    rating = string_to_float(line_data["Rating"])

    # Add 1 to counter if rating is above 4
    if rating > 4:
        number_of_museums = number_of_museums + 1

# Show the result
print("Number of museums with rating above 4:", number_of_museums)
