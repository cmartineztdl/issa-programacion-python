# Looking at “tripadvisor_museum_world.csv”, evaluate a way
# to check if the museum is from the USA.
# Discuss the weaknesses of your solution and implement a
# Python program that prints the country for each museum.

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

for line_data in input_reader:  # Loop to go through the data
    address = line_data["Address"]
    name = line_data["MuseumName"]

    list = address.split(",") # Split address with ","
    lastListElement = list[len(list) - 1].strip() # Get the last element
    countryCode = lastListElement[0:2] # Get the 2 fist chars

    if countryCode == countryCode.upper(): # Is EEUU
        print("(EEUU " + countryCode + ") " + address + " - " + name)
    else: ## Isn't EEUU
        print("(" + lastListElement + ") " + address + " - " + name)
