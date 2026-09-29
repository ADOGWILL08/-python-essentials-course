# data_processing.py
# Lab 4 - Part 2: Simulating data processing with functions, tuples, and dictionaries


def get_average_grade(grades_tuple):
    """
    Calculates the average of a tuple of numeric grades.

    Parameter:
        grades_tuple (tuple): a tuple of numbers (grades)
    Returns:
        The average (float) of the grades, or None if the tuple is empty.
    """
    try:
        # len() of an empty tuple is 0, and dividing by 0 raises ZeroDivisionError
        average = sum(grades_tuple) / len(grades_tuple)
        return average
    except ZeroDivisionError:
        # No grades to average, so there's nothing to divide
        print("Warning: no grades available to calculate an average.")
        return None


# A dictionary of courses, where each value is a tuple of grades for that course.
# History intentionally has an empty tuple, to test the empty-tuple edge case.
course_grades = {
    "Math": (85, 90, 78, 92),
    "Science": (70, 88, 95),
    "History": ()
}

print("Course averages:")
for course, grades_tuple in course_grades.items():
    average = get_average_grade(grades_tuple)

    # average is None when the course's tuple of grades was empty
    if average is None:
        print(f"The average grade for {course} could not be calculated (no grades).")
    else:
        print(f"The average grade for {course} is {average:.1f}")