heritage = 950000
segment_1 = 400000
segment_2 = 200000
tax_segment_1 = 0.00
tax_segment_2 = 0.03
tax_segment_3 = 0.05

# If is heritage is lower or equal than first segment
if heritage <= segment_1:
    total = segment_1 * tax_segment_1
# if is greater than segment 1 but lower than segment 3
elif heritage <= segment_1 + segment_2:
    total = segment_1 * tax_segment_1 + (heritage - segment_1) * tax_segment_2
# if heritage is greater than segment 2
else:
    total = segment_1 * tax_segment_1 + segment_2 * tax_segment_2 + (heritage - (segment_1 + segment_2)) * tax_segment_3

print("Total:", total)
