import random
import pandas as pd
from faker import Faker

# Set up Faker
fake = Faker(['en_NG'])  # Nigeria locale for Faker

# Generate Yoruba names
yoruba_first_names = ['Ayodele', 'Babatunde', 'Boluwatife', 'Damilola', 'Funmilayo', 'Ifeoluwa', 'Kehinde', 'Olamide', 'Olufunmilayo', 'Tayo']  # add 150 unique names
yoruba_last_names = ['Adebayo', 'Adeyemi', 'Adetokunbo', 'Akinbiyi', 'Akinyemi', 'Fadeyibi', 'Ogunleye', 'Oloruntobi', 'Omolayo', 'Oyetunde']  # add 150 unique names

# Helper function to pick weighted random choice
def weighted_choice(choices, weights):
    return random.choices(choices, weights=weights, k=1)[0]

# Generate Dim_Student table data
students = []
for _ in range(400):
    student = {
        'student_id': fake.unique.random_int(min=1, max=5000),
        'first_name': random.choice(yoruba_first_names),
        'last_name': random.choice(yoruba_last_names),
        'age': random.randint(13, 16),
        'gender': random.choice(['M', 'F']),
        'student_class': random.choice(['SS1', 'SS2', 'SS3']),
        'address_type': random.choice(['Rural', 'Urban']),
        'absent_times': weighted_choice([0, 1, 2, 3, 4, 5], [0.45, 0.45, 0.10, 0.0, 0.0, 0.0]),
        'goes_out_with_friends': random.choice([True, False]),
        'desire_higher_education': True,
        'family_support': 5,
        'internet_access': weighted_choice([True, False], [0.90, 0.10]),
        'commute_time': weighted_choice(range(5, 31), [0.80 if 5 <= x <= 20 else 0.20 for x in range(5, 31)]),
        'living_status': weighted_choice(['T', 'A'], [0.97, 0.03]),
        'time_spent_on_math': weighted_choice([3, 4, 5], [0.30, 0.35, 0.35]),
        'time_spent_on_english': weighted_choice([3, 4, 5], [0.30, 0.35, 0.35])
    }
    students.append(student)

# Generate Dim_Parent table data
parents = []
for _ in range(400):
    parent = {
        'parent_id': fake.unique.random_int(min=1, max=5000),
        'parent_income': weighted_choice([random.uniform(400000, 700000), random.uniform(700001, 800000)], [0.95, 0.05]),
        'mother_job': fake.job(),
        'father_job': fake.job()
    }
    parents.append(parent)

# Generate Dim_Teacher table data
teachers = []
for _ in range(50):  # Assuming 50 teachers
    teacher = {
        'teacher_id': fake.unique.random_int(min=1, max=100),
        'qualification': weighted_choice(['B.Sc', 'M.Sc'], [0.30, 0.70]),
        'teaching_method': weighted_choice(['Lecture', 'Practical'], [0.50, 0.50])
    }
    teachers.append(teacher)

# Generate Dim_School_Facilities table data
facilities = []
for _ in range(10):  # Assuming 10 facilities
    facility = {
        'facility_id': fake.unique.random_int(min=1, max=100),
        'facility_rating': weighted_choice([4, 5], [0.05, 0.95]),
        'library_access_hours': weighted_choice([3, 4, 5], [0.10, 0.45, 0.45]),
        'internet_availability': True
    }
    facilities.append(facility)

# Generate Fact_Student_Performance table data
performances = []
for i in range(400):
    performance = {
        'performance_id': fake.unique.random_int(min=1, max=5000),
        'student_id': students[i]['student_id'],
        'parent_id': parents[i]['parent_id'],
        'facility_id': random.choice(facilities)['facility_id'],
        'math_score': weighted_choice(range(49, 97), [0.02 if x < 55 else 0.98 for x in range(49, 97)]),
        'english_score': weighted_choice(range(49, 97), [0.02 if x < 55 else 0.98 for x in range(49, 97)])
    }
    performances.append(performance)

# Convert lists to DataFrames
df_students = pd.DataFrame(students)
df_parents = pd.DataFrame(parents)
df_teachers = pd.DataFrame(teachers)
df_facilities = pd.DataFrame(facilities)
df_performances = pd.DataFrame(performances)

# Save DataFrames to CSV files
df_students.to_csv('Dim_Student.csv', index=False)
df_parents.to_csv('Dim_Parent.csv', index=False)
df_teachers.to_csv('Dim_Teacher.csv', index=False)
df_facilities.to_csv('Dim_School_Facilities.csv', index=False)
df_performances.to_csv('Fact_Student_Performance.csv', index=False)

print("Data generation complete!")
