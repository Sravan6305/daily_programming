def get_marks(n):
    marks = []
    i = 0
    while i < n:
        m = int(input(f"Enter marks for subject {i+1}: "))
        if 0 <= m <= 100:
            marks.append(m)
            i += 1
        else:
            print("Invalid marks! Enter between 0 and 100.")
    return marks


def analyze(marks):
    total = 0
    fail = False

    for m in marks:
        total += m
        if m < 35:
            fail = True

    average = total / len(marks)
    percentage = average

    highest = marks[0]
    lowest = marks[0]
    high_sub = 1
    low_sub = 1

    for i in range(len(marks)):
        if marks[i] > highest:
            highest = marks[i]
            high_sub = i + 1
        if marks[i] < lowest:
            lowest = marks[i]
            low_sub = i + 1

    return total, average, percentage, highest, high_sub, lowest, low_sub, fail


def grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 35:
        return "D"
    else:
        return "F"



name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
n = int(input("Enter number of subjects: "))

name = name.capitalize()

marks = get_marks(n)

total, avg, perc, high, high_sub, low, low_sub, fail = analyze(marks)

result = "FAIL" if fail else "PASS"
final_grade = grade(perc)

print("      STUDENT REPORT      ")
print(f"Name: {name}")
print(f"Roll No: {roll}")
print(f"Marks: {marks}")
print(f"Total: {total}")
print(f"Average: {avg}")
print(f"Percentage: {perc}")
print(f"Highest: {high}")
print(f"Lowest: {low}")
print(f"Result: {result}")
print(f"Grade: {final_grade}")
