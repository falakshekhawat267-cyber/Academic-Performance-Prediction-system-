# Academic Performance Prediction SysteM

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample student data
# [Attendance %, Study Hours, Previous Marks %, Assignment %, Internal Marks %]

X = [
[90, 5, 85, 90, 88],
[80, 4, 75, 80, 78],
[70, 3, 65, 70, 68],
[95, 6, 90, 95, 92],
[60, 2, 50, 55, 52],
[85, 5, 80, 85, 82],
[55, 1, 45, 50, 48],
[75, 3, 70, 72, 69],
[92, 6, 88, 94, 90],
[65, 2, 58, 60, 55],
[88, 5, 82, 88, 85],
[50, 1, 40, 45, 42],
[78, 4, 72, 76, 74],
[94, 6, 91, 93, 95],
[68, 2, 60, 65, 62]
]

# 1 = Good Performance
# 0 = Needs Improvement

y = [1, 1, 0, 1, 0,1, 0, 1, 1, 0,1, 0, 1, 1, 0]

# Split data into training data and testing data
X_train, X_test, y_train, y_test = train_test_split
(X, y, test_size=0.2, random_state=42)

# Create the prediction model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n======================================")
print(" ACADEMIC PERFORMANCE PREDICTION")
print("======================================")

print("Model Accuracy:", round(accuracy,100,2), "%")

# Take the student details
print("\nEnter Student Details")

attendance = float(input("Attendance percentage: "))
study_hours = float(input("Average study hours per day: "))
previous_marks = float(input("Previous exam marks percentage: "))
assignment = float(input("Assignment completion percentage: "))
internal_marks = float(input("Internal marks percentage: "))

# Create the input for prediction
student = [[attendance,study_hours,previous_marks,assignment,internal_marks]]

# Make prediction
prediction = model.predict(student)

# Get probability
probability = model.predict_proba(student)

print("\n======================================")
print("     PREDICTION RESULT")
print("======================================")

if prediction[0] == 1:
  print("Performance: GOOD")
  print("The student is likely to perform well.")
else:
  print("Performance: NEEDS IMPROVEMENT")
  print("The student may need to improve their academic performance.")
  print("Prediction Confidence:",round(max(probability[0]), 100, 2),"%")

# Suggestions
  print("\nSuggestions:")

if attendance < 75:
  print("- Improve class attendance.")

if study_hours < 3:
  print("- Increase daily study time.")

if previous_marks < 60:
  print("- Focus on improving previous exam performance.")

if assignment < 70:
  print("- Complete assignments regularly.")

if internal_marks < 60:
  print("- Focus more on internal assessments.")

if (attendance >= 75 and study_hours >= 3 and previous_marks >= 60 and assignment >= 70 and internal_marks >= 60):
  print("- Keep up the good work!")
  print("======================================")