import numpy as np
import time


# TASK 1: Create an Array and Basic Math

# Create Celsius array
temps_celsius = np.array([22, 25, 28, 24, 26])

# Convert to Fahrenheit
temps_fahrenheit = temps_celsius * 1.8 + 32

# Calculate average Fahrenheit
avg_fahrenheit = round(np.mean(temps_fahrenheit), 1)


# Print results
print("Celsius:", temps_celsius)
print("Fahrenheit:", temps_fahrenheit)
print("Average Fahrenheit:", avg_fahrenheit)

###OUTPUT#######

# Celsius: [22 25 28 24 26]
# Fahrenheit: [71.6 77.  82.4 75.2 78.8]
# Average Fahrenheit: 77.0


# TASK 2: Array Shape and Statistics

scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print("Shape:", scores.shape)
print("Total elements:", scores.size)
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))
print("Range:", np.max(scores) - np.min(scores))


##output #######
# Celsius: [22 25 28 24 26]
# Fahrenheit: [71.6 77.  82.4 75.2 78.8]
# Average Fahrenheit: 77.0
# Shape: (12,)
# Total elements: 12
# Highest score: 95
# Lowest score: 76
# Range: 19

# TASK 3: Performance Comparison

# Create NumPy array
np_array = np.arange(1, 50001)

# Create Python list
py_list = list(range(1, 50001))

# NumPy sum timing
start_np = time.time()
np_sum = np.sum(np_array)
end_np = time.time()
np_time = end_np - start_np

# Python sum timing
start_py = time.time()
py_sum = sum(py_list)
end_py = time.time()
py_time = end_py - start_py

# Calculate speed difference
speed = py_time / np_time if np_time > 0 else 0

# Print results
print("NumPy sum:", np_sum)
print("Python sum:", py_sum)
print("NumPy time: {:.4f} seconds".format(np_time))
print("Python time: {:.4f} seconds".format(py_time))
print("NumPy is {:.1f}x faster".format(speed))


###OUTPUT#################33

# Celsius: [22 25 28 24 26]
# Fahrenheit: [71.6 77.  82.4 75.2 78.8]
# Average Fahrenheit: 77.0
# Shape: (12,)
# Total elements: 12
# Highest score: 95
# Lowest score: 76
# Range: 19
# NumPy sum: 1250025000
# Python sum: 1250025000
# NumPy time: 0.0000 seconds
# Python time: 0.0003 seconds
# NumPy is 7.1x faster