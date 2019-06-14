import math

point1x = float(raw_input("Point 1 X-value:"))
point1y = float(raw_input("Point 1 y-value:"))
point2x = float(raw_input("Point 2 x-value:"))
point2y = float(raw_input("Point 2 y-value:"))
def line_segment_length():
    length = math.sqrt(((point2x - point1x) ** 2) + ((point2y - point1y) ** 2))
    return length

#print line_segment_length()
def line_midpoint():
    x_value = ((point1x + point2x) / 2)
    y_value = ((point1y + point2y) / 2)
    midpoint = "(%s,%s)" % (x_value , y_value)
    return midpoint
#print line_midpoint()

def find_length_and_mid():
    return "Length: %s   Midpoint: %s" % (line_segment_length(), line_midpoint())
print find_length_and_mid()
