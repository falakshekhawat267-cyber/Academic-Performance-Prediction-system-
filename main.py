# Academic Performance Prediction System

print("==============================================")
print("   ACADEMIC PERFORMANCE PREDICTION SYSTEM")
print("==============================================")

# Taking student details
name = input("\nEnter Student Name: ")

attendance = float(input("Enter Attendance Percentage: "))
study_hours = float(input("Enter Average Study Hours per Day: "))
previous_marks = float(input("Enter Previous Exam Marks Percentage: "))
assignment = float(input("Enter Assignment Completion Percentage: "))
internal_marks = float(input("Enter Internal Marks Percentage: "))

# Calculate weighted performance score
score = (
attendance * 0.20 +
(study_hours / 8 * 100) * 0.15 +
previous_marks * 0.25 +
assignment * 0.15 +
internal_marks * 0.25
)

# Make sure score stays between 0 and 100
if score > 100:
score = 100

# Determine performance
if score >= 85:
performance = "Excellent"
message = "The student is performing exceptionally well."

elif score >= 70:
performance = "Good"
message = "The student is likely to perform well."

elif score >= 55:
performance = "Average"
message = "The student has average academic performance."

else:
performance = "Needs Improvement"
message = "The student needs to improve academic performance."

# Display result
print("\n==============================================")
print("              PREDICTION RESULT")
print("==============================================")

print("Student Name       :", name)
print("Performance Score  :", round(score, 2), "%")
print("Predicted Result   :", performance)
print("Message            :", message)

# Suggestions
print("\nSuggestions:")

suggestion_given = False

if attendance < 75:
print("- Improve class attendance.")
suggestion_given = True

if study_hours < 3:
print("- Increase daily study time.")
suggestion_given = True

if previous_marks < 60:
print("- Focus on improving previous exam marks.")
suggestion_given = True

if assignment < 70:
print("- Complete assignments regularly.")
suggestion_given = True

if internal_marks < 60:
print("- Focus more on internal assessments.")
suggestion_given = True

if suggestion_given == False:
print("- Keep up the good work!")

print("\n==============================================")
print("             Thank You!")
print("==============================================")