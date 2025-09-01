# ==========================
# Day 1: Python + NumPy + Pandas Exercises
# ==========================

# --------------------------
# Part 1: Python Basics
# --------------------------

# 1. Lists & Loops
numbers = [5, 10, 15, 20, 25]
print("Original numbers:", numbers)



# Multiply each number by 2
print("Numbers multiplied by 2:")
for num in numbers:
    print(num * 2)

# Sum all numbers
total = 0
for num in numbers:
    total += num
print("Sum of numbers:", total)

# 2. Dictionaries
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("\nStudent Scores:", students)

# Score of Bob
print("Score of Bob:", students["Bob"])

# Add a new student
students["David"] = 88
print("Updated Student Scores:", students)


# Loop through dictionary and print students with score > 85
print("Students with score > 85:")
for name, score in students.items():
    if score > 85:
        print(name, score)

# 3. Functions
def square(x):
    return x * x

print("\nSquare of 7:", square(7))

def average(lst):
    return sum(lst) / len(lst)

print("Average of numbers list:", average(numbers))

# # --------------------------
# # Part 2: NumPy Exercises
# # --------------------------
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("\nNumPy Array:", arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# Multiply all numbers by 3
arr_times3 = arr * 3
print("Array multiplied by 3:", arr_times3)

# --------------------------
# Part 3: Pandas Exercises
# --------------------------
import pandas as pd

# Create DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [20, 22, 19, 21, 23],
    "Score": [85, 90, 78, 88, 95]
}
df = pd.DataFrame(data)

print("\nDataFrame Head:")
print(df.head())

# Filter rows with Score > 80
high_scores = df[df["Score"] > 80]
print("\nStudents with Score > 80:")
print(high_scores)

# Average Score
avg_score = df["Score"].mean()
print("\nAverage Score:", avg_score)

# Add 'Passed' column
df["Passed"] = df["Score"] >= 50
print("\nDataFrame with Passed column:")
print(df)


