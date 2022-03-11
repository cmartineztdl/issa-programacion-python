heritage = 950000
segment_1 = 400000
segment_2 = 200000
tax_segment_1 = 0.00
tax_segment_2 = 0.03
tax_segment_3 = 0.05

# Calculate the amount in first segment
if(heritage <= segment_1):
    total_segment_1 = heritage
else:
    total_segment_1 = segment_1
# Calculate the remaining heritage
heritage = heritage - total_segment_1

# Calculate the amount in second segment
if(heritage <= segment_2):
    total_segment_2 = heritage
else:
    total_segment_2 = segment_2
# Calculate the remaining heritage
heritage = heritage - total_segment_2

# The remaining heritga is for the third segment
total_segment_3 = heritage

# Calculate the total
total_taxes_segment_1 = tax_segment_1 * total_segment_1
total_taxes_segment_2 = tax_segment_2 * total_segment_2
total_taxes_segment_3 = tax_segment_3 * total_segment_3
total = total_taxes_segment_1 + total_taxes_segment_2 + total_taxes_segment_3

# Show the total
print("Total:", total)
