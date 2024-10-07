import random
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker('en_NG')  # For Nigerian context

# Yoruba Names (150 sample first names and last names)
yoruba_first_names = [
    'Ayodele', 'Folake', 'Kehinde', 'Adeola', 'Babatunde', 'Oluwaseun', 'Funmilayo', 'Temitope', 'Olamide', 'Adebayo',
    # Add more names up to 150
]
yoruba_last_names = [
    'Akinyemi', 'Adelaja', 'Ige', 'Ogunleye', 'Olowokere', 'Adebayo', 'Adeyemi', 'Ojo', 'Oluwakemi', 'Bamigboye',
    # Add more names up to 150
]

# Function to generate students
def generate_students(num_records=400):
    student_data = []

    for _ in range(num_records):
        first_name = random.choice(yoruba_first_names)
        last_name = random.choice(yoruba_last_names)
        age = random.randint(13, 16)
        gender = random.choice(['M', 'F'])
        student_class = random.choice(['SS1', 'SS2', 'SS3'])
        address_type = random.choice(['Rural', 'Urban'])
        absent_times = random.choices([random.randint(7, 10), random.randint(0, 6)], [0.7, 0.3])[0]
        goes_out_with_friends = random.choice([True, False])
        desire_higher_education = random.choices([False, True], [0.65, 0.35])[0]
        family_support = random.choices([2, 3, random.choice([1, 4, 5])], [0.4, 0.4, 0.2])[0]
        internet_access = random.choices([False, True], [0.88, 0.12])[0]
        commute_time = random.choices([random.randint(30, 55), random.randint(25, 60)], [0.8, 0.2])[0]
        living_status = random.choices(['A', 'T'], [0.67, 0.33])[0]
        time_spent_on_math = random.choices([2, random.randint(1, 3)], [0.8, 0.2])[0]
        time_spent_on_english = random.choices([2, random.randint(1, 3)], [0.8, 0.2])[0]

        student_data.append({
            'student_id': _ + 1,
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'gender': gender,
            'student_class': student_class,
            'address_type': address_type,
            'absent_times': absent_times,
            'goes_out_with_friends': goes_out_with_friends,
            'desire_higher_education': desire_higher_education,
            'family_support': family_support,
            'internet_access': internet_access,
            'commute_time': commute_time,
            'living_status': living_status,
            'time_spent_on_math': time_spent_on_math,
            'time_spent_on_english': time_spent_on_english
        })

    return pd.DataFrame(student_data)

# Function to generate parents
def generate_parents(num_records=400):
    parent_data = []

    for _ in range(num_records):
        parent_income = random.choices([random.randint(50000, 150000), random.randint(151000, 300000)], [0.95, 0.05])[0]
        mother_job = fake.job()
        father_job = fake.job()

        parent_data.append({
            'parent_id': _ + 1,
            'parent_income': parent_income,
            'mother_job': mother_job,
            'father_job': father_job
        })

    return pd.DataFrame(parent_data)

# Function to generate teachers
def generate_teachers(num_records=50):
    teacher_data = []

    for _ in range(num_records):
        qualification = 'B.Sc'
        teaching_method = random.choices(['Lecture', 'Practical'], [0.95, 0.05])[0]

        teacher_data.append({
            'teacher_id': _ + 1,
            'qualification': qualification,
            'teaching_method': teaching_method
        })

    return pd.DataFrame(teacher_data)

# Function to generate school facilities
def generate_facilities(num_records=10):
    facility_data = []

    for _ in range(num_records):
        facility_rating = random.choices([1, 2, 3], [0.4, 0.55, 0.05])[0]
        library_access_hours = random.choices([0, 1, 2, 3], [0.3, 0.35, 0.2, 0.15])[0]
        internet_availability = random.choices([False, True], [0.94, 0.06])[0]

        facility_data.append({
            'facility_id': _ + 1,
            'facility_rating': facility_rating,
            'library_access_hours': library_access_hours,
            'internet_availability': internet_availability
        })

    return pd.DataFrame(facility_data)

# Function to generate student performance
def generate_student_performance(student_df, parent_df, facility_df):
    performance_data = []

    for student in student_df['student_id']:
        parent_id = random.choice(parent_df['parent_id'])
        facility_id = random.choice(facility_df['facility_id'])
        math_score = random.choices([random.randint(35, 54), random.randint(20, 34), random.randint(55, 70)], [0.85, 0.075, 0.075])[0]
        english_score = random.choices([random.randint(35, 54), random.randint(20, 34), random.randint(55, 70)], [0.85, 0.075, 0.075])[0]

        performance_data.append({
            'performance_id': student,
            'student_id': student,
            'parent_id': parent_id,
            'facility_id': facility_id,
            'math_score': math_score,
            'english_score': english_score
        })

    return pd.DataFrame(performance_data)

# Generate all tables
students = generate_students(400)
parents = generate_parents(400)
teachers = generate_teachers(50)
facilities = generate_facilities(10)
student_performance = generate_student_performance(students, parents, facilities)

# Save the generated datasets to CSV files
students.to_csv('students.csv', index=False)
parents.to_csv('parents.csv', index=False)
teachers.to_csv('teachers.csv', index=False)
facilities.to_csv('facilities.csv', index=False)
student_performance.to_csv('student_performance.csv', index=False)

print("Dataset generation complete.")
