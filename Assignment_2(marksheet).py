import turtle

name = input("Enter your Name: ")
program = input("Enter your Program Name: ")
age = input("Enter your Age: ")
gmail = input("Enter your Gmail: ")
university = input("Enter your University Name: ")

sub1 = int(input("Enter marks of Calculus: "))
sub2 = int(input("Enter marks of Programmig: "))
sub3 = int(input("Enter marks of English: "))
sub4 = int(input("Enter marks of ICT: "))
sub5 = int(input("Enter marks of Discret: "))
sub6 = int(input("Enter marks of Geometry: "))

total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
percentage = (total / 600) * 100

print("\nStudent Marksheet ")
print(f"Name: {name}")
print(f"Program: {program}")
print(f"Age: {age}")
print(f"Gmail: {gmail}")
print(f"University: {university}")

print(f"Subject 1 Marks: {sub1}")
print(f"Subject 2 Marks: {sub2}")
print(f"Subject 3 Marks: {sub3}")
print(f"Subject 4 Marks: {sub4}")
print(f"Subject 5 Marks: {sub5}")
print(f"Subject 6 Marks: {sub6}")

print(f"Total Marks: {total} / 600")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    grade = "A+"
    color = "green"
    result = "Pass "
elif percentage >= 70:
    grade = "A"
    color = "lightgreen"
    result = "Pass "
elif percentage >= 60:
    grade = "B"
    color = "blue"
    result = "Pass "
elif percentage >= 50:
    grade = "C"
    color = "orange"
    result = "Pass "
else:
    grade = "F"
    color = "red"
    result = "Fail"

print(f"Grade: {grade}")
print(f"Result: {result}")

# Use of Turtle Graphics to display grade

t = turtle.Turtle()
t.hideturtle()
t.pensize(5)
t.color(color)

t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)

t.penup()
t.goto(-30, 0)
t.write(grade, font=("Arial", 28, "bold"), align="left")

t.penup()
t.goto(-40, -40)
t.write(result, font=("Arial", 18, "bold"), align="left")

turtle.done()