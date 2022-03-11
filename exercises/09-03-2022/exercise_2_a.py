total_seconds = 96523

seconds_in_a_minute = 60
seconds_in_an_hour = seconds_in_a_minute * 60
seconds_in_a_day = seconds_in_an_hour * 24

seconds = total_seconds % seconds_in_a_minute
minutes = (total_seconds % seconds_in_an_hour) // seconds_in_a_minute
hours = (total_seconds % seconds_in_a_day) // seconds_in_an_hour
days = total_seconds // seconds_in_a_day

print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
