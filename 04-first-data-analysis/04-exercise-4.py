# 04-exercise-4
# 1. Using the dataset “tripadvisor_museum_world.csv”, get the name of the
# museum with the lowest number of reviews.
# 1. “Plan” your code/algorithm.
# 2. Implement.
# 3. Validate the result: Hungarian Natural History Museum

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

# Init the variables needed
museum_name = ""
number_of_reviews = 100000

for line_data in input_reader:  # Loop to go through the data
    # Get the number of reviews
    review_count = string_to_float(line_data["ReviewCount"])

    # Check if the actual museum has less reviews than the stored one
    if review_count < number_of_reviews:
        # Store the new review count
        number_of_reviews = review_count
        # Store the name of the museum
        museum_name = line_data["MuseumName"]


# Show the result
print("The museum with less reviews is:", museum_name)
print("  - Number of reviews:", int(number_of_reviews))
