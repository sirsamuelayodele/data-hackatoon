import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Parameters
num_students = 300

# Data containers
students = []
parents = []
school_facilities = []
performances = []

# Unique Yoruba names
first_names = ['Ayo', 'Tunde', 'Chidi', 'Kemi', 'Temi', 'Ola', 'Bola', 'Sade', 'Femi', 'Dayo', 'Tolu', 'Funmi', 'Bisi', 'Jide', 'Kola'] * 10  # Repeat to ensure 150 unique first names
last_names = ['Adeyemi', 'Afolabi', 'Ogunleye', 'Balogun', 'Ogunjobi', 'Okeke', 'Adesola', 'Abiola', 'Alabi', 'Ayodele', 'Oluwaseun', 'Adebayo', 'Ibrahim', 'Ojo', 'Osunade'] * 10  # Repeat to ensure 150 unique last names

for student_id in range(1, num_students + 1):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    # Generate student attributes
    address = random.choice(['Rural', 'Urban'])
    goes_out_with_friends = random.choice(['Yes', 'No'])
    desire_higher_education = 'Yes' if random.random() < 0.65 else 'No'
    family_support = random.choices([1, 2, 3, 4, 5], weights=[10, 10, 40, 40, 10])[0]
    commute_time = random.choices(range(5, 61), weights=[0.2] * 36 + [0.8] * 25)[0]  # 80% between 20 to 40 mins
    parent_income = random.choices(range(80000, 300001), weights=[0.97] * 101 + [0.03])[0]  # 97% between 100,000 to 200,000
    absent_times = random.choices(range(0, 11), weights=[0.7] * 7 + [0.3] * 4)[0]  # 70% between 0 to 6
    student_class = random.choice(['SS1', 'SS2', 'SS3'])
    
    students.append({
        'student_id': student_id,
        'first_name': first_name,
        'last_name': last_name,
        'address': address,
        'goes_out_with_friends': goes_out_with_friends,
        'desire_higher_education': desire_higher_education,
        'family_support': family_support,
        'commute_time': commute_time,
        'parent_income': parent_income,
        'absent_times': absent_times,
        'class': student_class,
    })

    # Generate parent attributes
    parents.append({
        'student_id': student_id,
        'mother_name': fake.name(),
        'father_name': fake.name(),
        'mother_job': fake.job(),
        'father_job': fake.job(),
    })

    # Generate school facility attributes
    school_facilities.append({
        'facility_id': student_id,
        'library_resources': random.choices(range(1, 6), weights=[0.1, 0.2, 0.4, 0.3])[0],  # 40% of facilities at 3, 30% at 4
        'internet_access': 'No' if random.random() < 0.55 else 'Yes',  # 55% to be No
        'sports_facilities': random.randint(1, 5),  # Rating between 1 to 5
        'classroom_condition': random.randint(1, 5),  # Rating between 1 to 5
    })

    # Generate performance attributes
    maths_score = random.choices(range(35, 81), weights=[0.15] * 16 + [0.85] * 12 + [0.03] * 3)[0]  # 85% between 51 to 63
    english_score = random.choices(range(35, 81), weights=[0.15] * 16 + [0.85] * 12 + [0.03] * 3)[0]  # 85% between 51 to 63

    performance_grade = 'C'
    if maths_score >= 64:
        performance_grade = 'B'
    if maths_score >= 70:
        performance_grade = 'A'

    performances.append({
        'student_id': student_id,
        'maths_score': maths_score,
        'english_score': english_score,
        'grade': performance_grade,
    })

# Create DataFrames for each table
students_df = pd.DataFrame(students)
parents_df = pd.DataFrame(parents)
school_facilities_df = pd.DataFrame(school_facilities)
performances_df = pd.DataFrame(performances)

# Save the DataFrames to CSV files
students_df.to_csv('students.csv', index=False)
parents_df.to_csv('parents.csv', index=False)
school_facilities_df.to_csv('school_facilities.csv', index=False)
performances_df.to_csv('performances.csv', index=False)

print("CSV files generated successfully.")
