import streamlit as st

# Function to calculate attendance
def calculate_attendance(absences):
    if absences >= 4:
        return "FAILED"
    else:
        return 100 - (absences * 10)

# Function to calculate class standing
def calculate_class_standing(quizzes, requirements, recitation):
    return (0.4 * quizzes) + (0.3 * requirements) + (0.3 * recitation)

# Function to calculate prelim grade
def calculate_prelim_grade(prelim_exam, attendance, class_standing):
    if attendance == "FAILED":
        return "FAILED"
    else:
        return (0.6 * prelim_exam) + (0.1 * attendance) + (0.3 * class_standing)

# Function to calculate required grades
def calculate_required_grades(prelim_grade, target_overall_grade):
    if prelim_grade == "FAILED":
        return "FAILED"
    else:
        required_midterm_grade = ((target_overall_grade - (0.2 * prelim_grade)) / 0.3) * 100
        required_finals_grade = ((target_overall_grade - (0.2 * prelim_grade) - (0.3 * required_midterm_grade)) / 0.5) * 100
        return required_midterm_grade, required_finals_grade

# Streamlit UI elements
st.title('Grade Calculator')

absences = st.number_input('Enter number of absences:', min_value=0, max_value=10, step=1)
prelim_exam = st.number_input('Enter Prelim Exam grade:', min_value=0.0, max_value=100.0, step=1.0)
quizzes = st.number_input('Enter Quizzes average:', min_value=0.0, max_value=100.0, step=1.0)
requirements = st.number_input('Enter Requirements grade:', min_value=0.0, max_value=100.0, step=1.0)
recitation = st.number_input('Enter Recitation grade:', min_value=0.0, max_value=100.0, step=1.0)

if st.button('Calculate'):
    attendance = calculate_attendance(absences)
    class_standing = calculate_class_standing(quizzes, requirements, recitation)
    prelim_grade = calculate_prelim_grade(prelim_exam, attendance, class_standing)

    if prelim_grade == "FAILED":
        st.error("Student has failed due to absences.")
    else:
        required_passing_grades = calculate_required_grades(prelim_grade, 75)
        required_deans_lister_grades = calculate_required_grades(prelim_grade, 90)
        
        st.success(f"Prelim Grade: {prelim_grade:.2f}")
        st.write(f"Required Midterm and Final Grades to pass with 75%: Midterm - {required_passing_grades[0]:.2f}, Finals - {required_passing_grades[1]:.2f}")
        st.write(f"Required Midterm and Final Grades to achieve Dean's Lister status with 90%: Midterm - {required_deans_lister_grades[0]:.2f}, Finals - {required_deans_lister_grades[1]:.2f}")
