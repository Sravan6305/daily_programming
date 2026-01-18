# Task 1: Unique Student Registry
# You’re given a list of student names (duplicates included).
# Requirements: Use a set to store unique student names.
# Create a dictionary where: key → student name, value → length of the student name
# Use dictionary methods like items() or get().

students = ["Ram", "Sam", "Ram", "John", "Sam"]

# unique_names = set(students)
# unique_student = {}
#
# for x in unique_names:
#     unique_student[x] = len(x)
#
# print(unique_student)


# TASK 2: Unique Attendance Register
# Concepts: set(), add(), len()
# You are given a list of student roll numbers (some repeated).
# Your job is to: Convert the list into a set. Add a new student roll number. Print the total number of unique students

# rolls = [101, 102, 103, 101, 104, 102]
# new_roll = 105
# roll_numbers = set(rolls)
# roll_numbers.add(new_roll)
# print(roll_numbers)


# TASK 3: Event Participants Cleanup
# Concepts: difference(), -, discard()
# Some people registered for an event but didn’t show up.
# Remove absent members. If "Z" is absent (even if not in set), remove it safely. Print final attendees
#
# registered = {"A", "B", "C", "D", "E"}
# absent = {"C", "E"}
#
# registered.removeAll('C')
# registered.remove('E')
# print(f'the final attendees are {registered}')


# TASK 4: Unique Subjects Tracker.
# You’re given a dictionary where keys are student names and values are lists of subjects.
# Task: Convert each student’s subject list into a set. Create a single set of all unique subjects.Count how many unique subjects exist.

# students = {"A": ["Math", "Physics", "Math"],"B": ["Physics", "Chemistry"],"C": ["Math", "Biology"]}
#
# subjects = set()
#
# for x in students.values():
#     subject_set = set(x)
#     subjects.update(subject_set)
#
# unique_subject_count = len(subjects)
#
# print(f'All unique subjects: {subjects}')
# print(f'Number of unique subjects: {unique_subject_count}')


