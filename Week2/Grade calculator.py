
# Student Grade Calculator
# Python Internship - Week 2

def get_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good effort! Keep practising!"
    elif marks >= 60:
        return "D", "You passed! Work hard to improve!"
    else:
        return "F", "Don't give up. Learn and try again!"


def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")


def main():
    print("=" * 40)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 40)

    name = input("Enter student name: ").strip()

    while name == "":
        print("Name cannot be empty!")
        name = input("Enter student name: ").strip()

    marks = get_valid_marks()

    grade, message = get_grade(marks)

    print("\n" + "=" * 40)
    print(f"📊 RESULT FOR {name.upper()}")
    print("=" * 40)
    print(f"Marks: {marks:g}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")
    print("=" * 40)

    print("\nThank you for using Student Grade Calculator!")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram stopped.")
    input("\nPress Enter to exit...")


