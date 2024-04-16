#Gabriela Fuller
#1/15/24
#DSC 430

#“I have not given or received any unauthorized assistance on this assignment”

#youtube linke:
#https://youtu.be/ipcr1ip9x7c

def graded_assignment():
    #defines the function, the starting point 

    # Initial grade
    grade = 0

    # Check basic requirements
    if not check_basic_requirements():
        return grade  # No need to proceed if basic requirements are not met

    # Award points for code quality and video
    code_grade = award_code_points()
    video_grade = award_video_points()
    grade = code_grade + video_grade

    # Check for late submission
    if is_late():
        grade = apply_late_penalty(grade)

    return grade
print("Answer by only typing [Y/n]")
uncompressed = input(
    "Assignment submitted as a single uncompressed .py file? ").lower()
namedate = input("Assignment include the author's name and date? ").lower()
if namedate == "n":
    exit(0)
honorstmt = input("Assignment include honor statement? ").lower()
video = input("Assignment include 3-minute video? ").lower()

grade = 0
if uncompressed == "y" and namedate == "y" and honorstmt == "y" and video == "y":
    grade += int(input("how would you evaluate the correctness of the code? /10 points "))
    grade += int(input("how would you evaluate the elegance of the code? /10 points "))
    grade += int(input("Out of 10 points, how would you evaluate the code hygiene? /10 points"))
    grade += int(input("Out of 10 points, how would you evaluate the quality of discussion? /10 points"))
    late = input("Is assignment late subitted? y/n").lower()
    if late == "y":
        time = int(input("How late it is? "))
        grade = grade - (grade * time/100)
    print("\nTotal grade :", grade)
else:
    print("\nTotal grade :", grade)
