# Having a string that represents a date in “yyyy-mm-dd”
# format, create a program that prints the year, month and day.

# With split
aDate = "2022-04-06"
list = aDate.split("-")

print("Year:", list[0])
print("Month:", list[1])
print("Day:", list[2])

print("------------------------")

# With string index
print("Year:", aDate[0:4])
print("Month:", aDate[5:7])
print("Day:", aDate[8:10])