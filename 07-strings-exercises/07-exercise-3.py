# Having a string that represents a date in “yyyy-mm-dd”
# format, create a program that prints the month name.
# e.g. “2022-02-25” will print “February”.

aDate = "2022-03-25"

# month = aDate[5:7]
month = aDate.split("-")[1]

print("Month number:", month)

# if month == "01":
#     print("Month:", "Jan")
# if month == "02":
#     print("Month:", "Feb")
# if month == "03":
#     print("Month:", "Mar")
# if month == "04":
#     print("Month:", "Apr")
# if month == "05":
#     print("Month:", "May")
# if month == "06":
#     print("Month:", "Jun")
# if month == "07":
#     print("Month:", "Jul")
# # if month == "08":
#     print("Month:", "Aug")
# if month == "09":
#     print("Month:", "Sep")
# if month == "10":
#     print("Month:", "Oct")
# if month == "11":
#     print("Month:", "Nov")
# if month == "12":
#     print("Month:", "Dec")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
print("Month:", months[int(month) - 1]) 