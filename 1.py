import turtle
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("\tSTUDENT MARKSHEET SYSTEM")

def per_info():
    student_name = input("Enter your Name: ").title()
    father_name = input("Enter Father Name: ").title()
    program = input("Enter your Program Name: ").upper()
    gmail = input("Enter your Gmail: ")
    university = input("Enter your University Name: ").title()
    student_id = input("Enter your Student ID: ")

    print("\nEnter Marks for the following subjects (out of 100):")
    subjects = ["Calculus", "English", "Discrete", "PF", "I&CT"]
    marks = {}

    for subject in subjects:
        while True:
            try:
                score = float(input(f"{subject}: "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks.values())
    average = total / len(subjects)
    percentage = (total / (len(subjects) * 100)) * 100

    if 80 <= percentage <= 100:
        grade = "A+"
    elif 70 <= percentage < 80:
        grade = "A"
    elif 60 <= percentage < 70:
        grade = "B"
    elif 50 <= percentage < 60:
        grade = "C"
    elif 40 < percentage < 50:
        grade = "D"
    else:
        grade = "F"

    result = "Pass" if percentage >= 40 else "Fail"

    print("\n\tSTUDENT MARKSHEET")
    print(f"Name: {student_name}")
    print(f"Father Name: {father_name}")
    print(f"Program: {program}")
    print(f"University: {university}")
    print(f"Student ID: {student_id}")
    print(f"Gmail: {gmail}")

    print("\nSubject Marks:")
    for sub, val in marks.items():
        print(f"   {sub:<10}: {val}/100")

    print(f"\nTotal Marks: {total}/500")
    print(f"Average Marks: {average:.2f}")
    print(f"Percentage: {percentage:.2f}%")

    color = "\033[92m" if result == "Pass" else "\033[91m"
    reset = "\033[0m"
    print(f"Grade: {color}{grade}{reset}")
    print(f"Result: {color}{result}{reset}")

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Student Result")

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.pensize(5)
    pen.speed(5)

    if result == "Fail":
        pen.color("red")
        pen.penup()
        pen.goto(0, -100)
        pen.pendown()
        pen.circle(120)
        pen.penup()
        pen.goto(0, -85)
        pen.pencolor("red")
        pen.write("F", align="center", font=("Arial", 130, "bold"))
    else:
        pen.color("green")
        pen.penup()
        pen.goto(0, -100)
        pen.pendown()
        pen.circle(120)
        pen.penup()
        pen.goto(0, -85)
        pen.pencolor("green")
        pen.write("P", align="center", font=("Arial", 130, "bold"))

    time.sleep(1)
    turtle.done()



def signup():
    per_info()

def signIn():
    per_info()

