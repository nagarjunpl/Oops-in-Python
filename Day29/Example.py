from functools import reduce

scores = [50, 35, 67, 90, 40, 70, 95, 88, 85]

# Add 5 bonus points to each score using map
updated = list(map(lambda x: x + 5, scores))

# Filter scores that are 50 or above using filter
passed = list(filter(lambda x: x >= 50, updated))

# Calculate the total of passed scores using reduce
total = reduce(lambda x, y: x + y, passed)


print("Updated Scores:", updated)
print("Passed Scores:", passed)
print("Total of Passed Scores:", total)