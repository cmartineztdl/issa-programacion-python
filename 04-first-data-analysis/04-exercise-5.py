# 04-exercise-5
# Using the dataset “tripadvisor_museum_world.csv”, count the museums with a
# number of reviews bellow the average review number value.
# 1. “Plan” your code/algorithm.
# 2. Implement.
# 3. Validate the result: 799

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
# Transform the iterator into a list
data = list(input_reader)

# Init the variables needed
number_of_museums = 0
total_of_reviews = 0

for line_data in data:  # Loop to go through the data
    # Get the number of reviews
    review_count = string_to_float(line_data["ReviewCount"])

    # Update the counters
    number_of_museums = number_of_museums + 1
    total_of_reviews = total_of_reviews + review_count

# Calculate average
number_of_reviews_average = total_of_reviews / number_of_museums

# Show average
print("Number of reviews average:", number_of_reviews_average)

# Init count for museums with more reviews than the average
museums_below_average = 0
for line_data in data:  # Loop to go through the data
    # Get the number of reviews
    review_count = string_to_float(line_data["ReviewCount"])

    # Increase counter if has more than average
    if review_count < number_of_reviews_average:
        museums_below_average = museums_below_average + 1

# Show the result
print("Museums with a number of reviews bellow the average:", museums_below_average)
