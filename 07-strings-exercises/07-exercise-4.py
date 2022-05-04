# Using "tripadvisor_museum_world.csv", create a Python
# program that gets the number of museums for each number
# of features ("FeatureCount" column)

import csv


def string_to_int(v):
    try:
        v = v.replace(',', '')
        return int(v)
    except Exception:
        return 0


# Open the data file
input_file = open('datasets/tripadvisor_museum_world.csv', encoding='utf-8')
# Create a "reader" to go through the data
input_reader = csv.DictReader(input_file)
lines = list(input_reader)

max_feature_count = 0

for line_data in lines:  # Loop to go through the data
    feature_count = string_to_int(line_data["FeatureCount"])

    if feature_count > max_feature_count:
        max_feature_count = feature_count

print("Max feature count:", max_feature_count)

count = [0] * (max_feature_count + 1)

for line_data in lines:  # Loop to go through the data
    feature_count = string_to_int(line_data["FeatureCount"])

    count[feature_count] = count[feature_count] + 1

print(count)

for i in range(len(count)):
    if count[i] > 0:
        print("Museums with", i, "feature count:", count[i])