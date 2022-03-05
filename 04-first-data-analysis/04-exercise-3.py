# 04-exercise-3
# 1. Get the number of museums grouped by number of reviews
# (<1000, 1000 to 10000,>10000).
# 1. “Plan” your code/algorithm.
# 2. Implement.
# 3. Validate the result:
#   - <1000: 110
#   - 1000 to 10000: 432
#   - >10000: 470

# OJO! Los valores no coinciden, está mal o el enunciado o el resultado del PDF

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

# Init the counters to count number of museums
less_than_1000 = 0
between_1000_and_10000 = 0
more_than_10000 = 0

for line_data in input_reader:  # Loop to go through the data
    # Get the number of reviews
    review_count = string_to_float(line_data["ReviewCount"])

    # Add 1 to counter if rating is above 4 and more than 1000 reviews
    if review_count < 1000:
        less_than_1000 = less_than_1000 + 1
    elif 1000 <= review_count and review_count <= 10000:
        between_1000_and_10000 = between_1000_and_10000 + 1
    else:
        more_than_10000 = more_than_10000 + 1

# Show the result
print("Number of museums with more than 10000 reviews:", more_than_10000)
print("Number of museums between 1000 and 10000 reviews:", between_1000_and_10000)
print("Number of museums with less than 1000 reviews:", less_than_1000)
