def grade_system():
    """Collect 5 marks, calculate average, and display letter grade."""
    marks = []  # list to store marks

    # Get 5 valid marks from user
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter mark {i+1}: "))
                # Check if mark is within valid range
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break  # exit the while loop, move to next mark
                else:
                    print("Mark must be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Calculate average
    average = sum(marks) / len(marks)

    # Determine grade
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Display result
    print(f"\nAverage: {average:.2f} - Grade: {grade}")

# Call the function to test (this line is now OUTSIDE the function)
grade_system()