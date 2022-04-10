import csv

# Museums with rating 5
# Show name, review count

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
    rating = string_to_float(line_data["Rating"])
    review_count = string_to_float(line_data["ReviewCount"])
    name = line_data["MuseumName"]

    if rating == 5:
        print(name, review_count)