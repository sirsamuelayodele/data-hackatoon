import random
import pandas as pd
from faker import Faker

# Initialize Faker instance
fake = Faker()

# Custom Yoruba first and last names (150 unique samples each)
yoruba_first_names = ['Adetola', 'Ayodeji', 'Bolaji', 'Damilola', 'Eniola', 'Femi', 'Gbemisola', 'Ifeoluwa', 'Jumoke', 'Kehinde', 'Ladejobi', 'Mojisola', 'Oladapo', 'Omotola', 'Pelumi'] * 10
yoruba_last_names = ['Adebayo', 'Adekunle', 'Adesanya', 'Ajayi', 'Babalola', 'Balogun', 'Fashola', 'Ibrahim', 'Johnson', 'Ogunleye', 'Okunola', 'Olumide', 'Onasanya', 'Oseni', 'Sule'] * 10

# Helper function for weighted random choice
def weighted_choice(choices, weights):
    return random.choices(choices, weights=weights, k=1)[0]

# Data generation for 400 students
students_data = []
for _ in range(400):
    student_id = fake.unique.random_int(min=1, max=5000)
    first_name = random.choice(yoruba_first_names)
    last_name = random.choice(yoruba_last_names)
    age = random.randint(13, 16)
    gender = random.choice(['M', 'F'])
    student_class = random.choice(['SS1', 'SS2', 'SS3'])
    address_type = random.choice(['Rural', 'Urban'])
    absent_times = weighted_choice([0, 1, 2, 3, 4, 5, 6, 7], [10, 10, 10, 10, 10, 15, 15, 10])  # 40% for 5-7, 60% for others
    goes_out_with_friends = random.choice([True, False])
    desire_higher_education = weighted_choice([True, False], [0.75, 0.25])
    family_support = weighted_choice([2, 3, 4, 5], [0.2, 0.6, 0.1, 0.1])  # 60% for 3, 20% for 2
    internet_access = weighted_choice([True, False], [0.52, 0.48])
    commute_time = weighted_choice(list(range(20, 51)), [0.8 if 20 <= x <= 35 else 0.2 for x in range(20, 51)])
    living_status = weighted_choice(['T', 'A'], [0.7, 0.3])
    time_spent_on_math = weighted_choice([2, 3, 4], [0.3, 0.35, 0.35])  # 30% for 2 hours
    time_spent_on_english = weighted_choice([2, 3, 4], [0.3, 0.35, 0.35])  # Same for English

    students_data.append({
        'student_id': student_id,
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

# Data generation for 400 parents
parents_data = []
for _ in range(400):
    parent_id = fake.unique.random_int(min=1, max=5000)
    parent_income = weighted_choice([random.uniform(100000, 300000), random.uniform(300001, 400000)], [0.95, 0.05])
    mother_job = fake.job()
    father_job = fake.job()

    parents_data.append({
        'parent_id': parent_id,
        'parent_income': parent_income,
        'mother_job': mother_job,
        'father_job': father_job
    })

# Data generation for 400 school facilities
facilities_data = []
for _ in range(400):
    facility_id = fake.unique.random_int(min=1, max=5000)
    facility_rating = weighted_choice([2, 3, 4], [0.2, 0.4, 0.4])  # 40% for 3, 60% for others
    library_access_hours = weighted_choice([1, 2, 3], [0.45, 0.45, 0.1])  # 45% for 1 and 2, 10% for 3
    internet_availability = weighted_choice([True, False], [0.56, 0.44])

    facilities_data.append({
        'facility_id': facility_id,
        'facility_rating': facility_rating,
        'library_access_hours': library_access_hours,
        'internet_availability': internet_availability
    })

# Data generation for student performance
performance_data = []
for student in students_data:
    performance_id = fake.unique.random_int(min=1, max=5000)
    student_id = student['student_id']
    parent_id = random.choice(parents_data)['parent_id']
    facility_id = random.choice(facilities_data)['facility_id']
    math_score = weighted_choice(list(range(39, 89)), [0.85 if 39 <= x <= 64 else 0.15 for x in range(39, 89)])
    english_score = weighted_choice(list(range(39, 89)), [0.85 if 39 <= x <= 64 else 0.15 for x in range(39, 89)])

    performance_data.append({
        'performance_id': performance_id,
        'student_id': student_id,
        'parent_id': parent_id,
        'facility_id': facility_id,
        'math_score': math_score,
        'english_score': english_score
    })

# Convert to pandas DataFrames
df_students = pd.DataFrame(students_data)
df_parents = pd.DataFrame(parents_data)
df_facilities = pd.DataFrame(facilities_data)
df_performance = pd.DataFrame(performance_data)

# Save to CSV
df_students.to_csv('students.csv', index=False)
df_parents.to_csv('parents.csv', index=False)
df_facilities.to_csv('facilities.csv', index=False)
df_performance.to_csv('performance.csv', index=False)

print("Data generated and saved successfully!")
