"""
✅ Grade Calculator:
Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
input- score - 89
output- B
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59

"""

score = int(input("Enter your score\n"))
#score >=90 and score <=100 -> A
#score >=80 and score <=89 -> B

if score >= 90 and score <= 100:   #Smiplified chain format -> 90 <= Score >= 100
    print("Your Grade is ","A")
elif score >= 80 and score <= 89:
    print("Your Grade is ","B")
elif score >= 70 and score <= 79:
    print("Your Grade is ","C")
elif score >= 60 and score <= 69:
    print("Your Grade is ","D")
elif score >= 101:
    print("You are Superman!")
else:
    grade = "F"
    print("Your Grade is ", grade)