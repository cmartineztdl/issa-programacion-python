seconds = 4001 * 24

seconds_in_a_minute = 60
seconds_in_an_hour = seconds_in_a_minute * 60
seconds_in_a_day = seconds_in_an_hour * 24

days = seconds // seconds_in_a_day

seconds = seconds - days * seconds_in_a_day

hours = seconds // seconds_in_an_hour

seconds = seconds - hours * seconds_in_an_hour

minutes = seconds // seconds_in_a_minute

seconds = seconds - minutes * seconds_in_a_minute

print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)