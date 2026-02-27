# ===================================
# TASK 1: CREATE AND WRITE STUDENT DATA
# ===================================
# Task 1: Create and Write Student Data

file = open("students.txt", "w")

file.write("Alice,85\n")
file.write("Bob,92\n")
file.write("Charlie,78\n")
file.write("Diana,95\n")

file.close()

print("Student data written successfully.")

# ===================================
# TASK 2: READ AND DISPLAY DATA
# ===================================
# Task 2: Read and Display Data

try:
    with open("students.txt", "r") as file:
        lines = file.readlines()
        
        for line in lines:
            name, score = line.strip().split(",")
            print(f"Student: {name}, Score: {score}")

except FileNotFoundError:
    print("Error: students.txt file not found.")

# ===================================
# TASK 3: APPEND NEW STUDENT AND CREATE LOG
# ===================================
# Task 3: Append new student

# Append new student record
with open("students.txt", "a") as file:
    file.write("Eve,88\n")

# Create activity log
with open("activity.log", "w") as log:
    log.write("Added new student: Eve\n")

print("New student added and activity logged.")
