import grades

LAST_NAME = "Polinar"
STUDENT_ID = "TUPM-25-4493"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

scores = [
    SEED_DIGIT * 10,
    ID_SUM % 100,
    NAME_LENGTH * 7
]

average = grades.compute_average(scores)
grade = grades.assign_grade(average)
remark = grades.generate_remark(grade)

print("=" * 40)
print(f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print(f"Generated Scores: {scores}")
print(f"Average: {round(average,2)}")
print(f"Grade: {grade}")
print(f"Remark: {remark}")
print("=" * 40)

SEED_NUM = 3
FAVORITE_ARTIST = "TAYLORSWIFT"
CONTROL_NUM = max(1, SEED_NUM)

from access_control import compute_access_level, validate_access

SEED_NUM = 7  # change this
FAVORITE_ARTIST = "TAYLORSWIFT"  # change this
CONTROL_NUM = max(1, SEED_NUM)

# Compute
access_level = compute_access_level(CONTROL_NUM, FAVORITE_ARTIST)
threshold = CONTROL_NUM * 5

# Validate
decision = validate_access(access_level, threshold)

# Print required assessment data
print("CONTROL_NUM Used:", CONTROL_NUM)
print("FAVORITE_ARTIST Length:", len(FAVORITE_ARTIST))
print("Computed Access Level:", access_level)
print("Threshold Applied:", threshold)
print("Final Authorization Decision:", decision)

from media_engine import process_stream

limit = CONTROL_NUM + len(FAVORITE_ARTIST)

total_plays, records = process_stream(limit)

print("Computed Stream Limit:", limit)
print("Total Plays:", total_plays)
print("Number of Records Processed:", records)

