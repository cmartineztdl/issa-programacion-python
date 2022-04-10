import csv

# tripadvisor_museum_world.csv
#  * More than 5 features
#  * Rating above 4

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

for line_data in input_reader:  # Loop to go through the data
    features = string_to_float(line_data["FeatureCount"])
    rating = string_to_float(line_data["Rating"])
    name = line_data["MuseumName"]

    if features > 5 and rating > 4:
        print(name, features, rating)
