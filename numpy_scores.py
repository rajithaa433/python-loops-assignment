import numpy as np

#Task 1 — Generate and Inspect Data
# Set seed
np.random.seed(42)

# Generate scores (5 students × 4 subjects)
scores = np.random.randint(50, 101, size=(5, 4))

print("Scores:\n", scores)

# 3rd student, 2nd subject (index 2,1)
print("3rd student, 2nd subject:", scores[2, 1])

# Last 2 students (all subjects)
print("Last 2 students:\n", scores[-2:, :])

# First 3 students, subjects 2 and 3 (index 1 and 2)
print("First 3 students, subjects 2 & 3:\n", scores[:3, 1:3])

#Task 2 — Analyze with Broadcasting
# Column-wise mean (per subject)
col_mean = np.round(scores.mean(axis=0), 2)
print("Column-wise mean:", col_mean)

# Add curve using broadcasting
curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve

# Ensure no score exceeds 100
curved_scores = np.clip(curved_scores, None, 100)

print("Curved Scores:\n", curved_scores)

# Row-wise max (best subject per student)
row_max = curved_scores.max(axis=1)
print("Best subject per student:", row_max)
#Task 3 — Normalize and Identify

# Row-wise min and max
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)

# Min-max normalization per row
normalized = (curved_scores - row_min) / (row_max - row_min)

print("Normalized Scores:\n", normalized)

# Find index of highest normalized value
max_index = np.unravel_index(np.argmax(normalized), normalized.shape)
print("Student index and subject index of highest value:", max_index)

# Extract all scores strictly above 90
above_90 = curved_scores[curved_scores > 90]
print("Scores above 90:", above_90)