def grade_calculator():
    print("------ Grade Calculator ------")

    # Input number of subjects
    n = int(input("Enter the number of subjects: "))

    marks = []
    for i in range(n):
        score = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(score)

    # Calculate total and average
    total = sum(marks)
    average = total / n
    percentage = (total / (n * 100)) * 100  # assuming each subject is out of 100

    # Determine grade
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Display results
    print("\n------ Results ------")
    print(f"Total Marks: {total}/{n*100}")
    print(f"Average Marks: {average:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


# Run the program
grade_calculator()