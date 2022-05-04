# Looking at “tripadvisor_museum_world.csv”, evaluate a way
# to check if the museum is from the USA.
# Discuss the weaknesses of your solution and implement a
# Python program that prints the country for each museum.

import csv
from itertools import count


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

cont = {}

# Qinling North Road, Lintong District, Xi'an 710600, China (Formerly The Terracotta Army,Terra Cotta Warriors and Horses)	
# 	527 Chayamachi, Higashiyama-ku, Kyoto 605-0931, Kyoto Prefecture
for line_data in input_reader:  # Loop to go through the data
    address = line_data["Address"]

    list = address.split(",") # Split address with ","
    lastListElement = list[len(list) - 1].strip() # Get the last element
    countryCode = lastListElement[0:2] # Get the 2 fist chars

    country = ""
    if countryCode == countryCode.upper(): # Is EEUU
        country = "EEUU"
    elif lastListElement.endswith("Prefecture"):
        country = "Japan"
    else: ## Isn't EEUU
        country = lastListElement
        country = country.split("(")[0].strip() #Removes

    if country in cont:
        cont[country] = cont[country] + 1
    else:
        cont[country] = 1

for country in cont:
    print(country, cont[country], sep=" -> ")


