
def check_grade():
    try:
        score = float(input("Enter your score (0-100): "))

        if score < 0 or score > 100:
            print("Invalid score! Please enter a score between 0 and 100.")
        elif score >= 90:
            print("Your grade is: A")
        elif score >= 80:
            print("Your grade is: B")
        elif score >= 70:
            print("Your grade is: C")
        elif score >= 60:
            print("Your grade is: D")
        else:
            print("Your grade is: F")

    except ValueError:
        print("Invalid input! Please enter a numeric score.")


if __name__ == "__main__":
    check_grade()
