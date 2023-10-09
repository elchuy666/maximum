data = [1.0, 3.14, 6.2, 0.1, 5.3]

minimum = 99999.99
for x in data:
    if x < minimum:
        minimum = x
    #print(x)

print(minimum)