import random
import faker
import pandas as pd

# Initialize Faker
fake = faker.Faker('en_NG')  # Nigerian locale for realistic context

# Define 150 unique Yoruba first names and 150 unique Yoruba last names
yoruba_first_names = [
    'Adebayo', 'Adetokunbo', 'Adeola', 'Adeshola', 'Adetunji', 'Ademola', 
    'Folake', 'Olufunke', 'Tunde', 'Kehinde', 'Taiwo', 'Yejide', 
    'Femi', 'Oluwaseun', 'Olamide', 'Temitope', 'Bukola', 'Damilola', 
    'Ayotunde', 'Ireoluwa', 'Tosin', 'Seun', 'Dayo', 'Modupe', 
    'Opeyemi', 'Olawale', 'Chinonso', 'Chidera', 'Emeka', 'Obinna', 
    'Kenechukwu', 'Ifedayo', 'Tobiloba', 'Oyinlola', 'Tolu', 'Ojo', 
    'Folorunsho', 'Olatunde', 'Olatunji', 'Oluwatobi', 'Oluwatimilehin', 
    'Oluwanifemi', 'Ayo', 'Yinka', 'Temiloluwa', 'Akin', 'Mide', 
    'Yemi', 'Seyi', 'Dayo', 'Kiki', 'Fiyinfoluwa', 'Damilare', 
    'Yejide', 'Titilayo', 'Jibola', 'Oluwakemi', 'Olajumoke', 
    'Abiola', 'Olasunkanmi', 'Adeyemi', 'Temitope', 'Oluwanisola', 
    'Oluwasemilore', 'Funmilola', 'Eniola', 'Moyosore', 'Toyin', 
    'Adewale', 'Abike', 'Anu', 'Doyin', 'Omolara', 'Ayanfe', 
    'Olamijuwon', 'Folarin', 'Oluwatofunmi', 'Adunola', 'Ireti', 
    'Afolabi', 'Temilade', 'Yetunde', 'Oreoluwa', 'Ayoade', 
    'Bimpe', 'Ibukun', 'Kehinde', 'Oluwatobiloba', 'Amarachi', 
    'Adebisi', 'Oni', 'Ojo', 'Ayanfe', 'Afolabi', 'Boluwatife', 
    'Simi', 'Abike', 'Tawakalitu', 'Temitope', 'Dapo', 'Modupe', 
    'Afishetan', 'Oluwaseun', 'Fatimah', 'Deola', 'Bola', 
    'Titi', 'Oluwaseun', 'Lanre', 'Bola', 'Fadekemi', 
    'Micheal', 'Samuel', 'Ikechukwu', 'Chike', 'Chukwudi', 
    'Chijioke', 'Micheal', 'Philip', 'Abubakar', 'Ali', 
    'Usman', 'Sadiq', 'Musa', 'Zainab', 'Aisha', 
    'Fatima', 'Hauwa', 'Bashir', 'Halima', 'Kabir', 
    'Zahra', 'Yusuf', 'Olayemi', 'Ibraheem', 'Khadijat'
]

yoruba_last_names = [
    'Adebola', 'Adeyemi', 'Adelani', 'Adedoyin', 'Afolabi', 'Alabi', 
    'Bello', 'Dada', 'Emmanuel', 'Ogunleye', 'Okwuosa', 'Akanbi', 
    'Oba', 'Olajide', 'Olaoye', 'Olasunkanmi', 'Olujimi', 
    'Olofinjana', 'Oluwatoyin', 'Olatunji', 'Okoro', 'Okunola', 
    'Okwuosa', 'Olayiwola', 'Oni', 'Salami', 'Saliu', 
    'Shodipo', 'Sulaimon', 'Tajudeen', 'Umar', 'Yusuf', 
    'Zubair', 'Omoniyi', 'Alabi', 'Adedayo', 'Adelakun', 
    'Abdul', 'Abubakar', 'Abiola', 'Alabi', 'Adetunji', 
    'Ayobami', 'Emeka', 'Ibrahim', 'Izuchukwu', 'Nwachukwu', 
    'Obinna', 'Okwuosa', 'Okwudili', 'Onyeabor', 'Onyemaechi', 
    'Tijani', 'Wale', 'Yekini', 'Abidemi', 'Adeagbo', 
    'Adelani', 'Ajayi', 'Akinyemi', 'Ali', 'Amadi', 
    'Azeez', 'Chukwuma', 'Chinyere', 'Chinonso', 'Chuka', 
    'Daniel', 'Ehi', 'Emeka', 'Fadipe', 'Fola', 
    'Gideon', 'Ibe', 'Igbinosa', 'Innocent', 'Iru', 
    'Joshua', 'Kehinde', 'Moses', 'Nnaji', 'Nwanne', 
    'Obinna', 'Oghenero', 'Okwudili', 'Oluoch', 'Olayiwola', 
    'Oni', 'Osawe', 'Ozuru', 'Ozuru', 'Suleiman', 
    'Tade', 'Tajudeen', 'Temitope', 'Wasiu', 'Yekeen'
]

# Define weighted random selection function
def weighted_choice(options, weights):
    return random.choices(options, weights)[0]

# Generate student name from Yoruba names only
def generate_student_name():
    first_name = random.choice(yoruba_first_names)
    last_name = random.choice(yoruba_last_names)
    return first_name, last_name

# Generate age based on student class
def generate_age(student_class):
    if student_class == 'SS1':
        return random.randint(13, 14)
    elif student_class == 'SS2':
        return random.randint(14, 16)
    else:
        return random.randint(15, 18)

# Create empty lists to hold the records for each table
students = []
parents = []
teachers = []
school_facilities = []
performances = []

# Generate data for 300 students
for student_id in range(1, 301):
    # Generate student name and attributes
    first_name, last_name = generate_student_name()
    student_class = random.choice(['SS1', 'SS2', 'SS3'])  # Class selection
    age = generate_age(student_class)
    gender = random.choice(['Male', 'Female'])
    absent_times = weighted_choice([0, 1, 2, 3, 4, 5], [0.45, 0.45, 0.10, 0.01, 0.01, 0.01])  # 90% between 0 and 2
    address_type = random.choice(['Rural', 'Urban'])
    goes_out_with_friends = random.choice(['Yes', 'No'])
    desire_higher_education = 'Yes'  # 100% Yes
    family_support = weighted_choice(range(4, 6), [0.05, 0.95])  # 95% at 5
    internet_access = 'Yes'  # 100% Yes
    commute_time = weighted_choice(range(5, 21), [0.8] * 6 + [0.2] * 16)  # 80% between 5 and 10 mins
    living_status = weighted_choice(['T', 'A'], [0.33, 0.67])  # 67% A

    students.append({
        'student_id': student_id,
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'gender': gender,
        'student_class': student_class,
        'absent_times': absent_times,
        'address_type': address_type,
        'goes_out_with_friends': goes_out_with_friends,
        'desire_higher_education': desire_higher_education,
        'family_support': family_support,
        'internet_access': internet_access,
        'commute_time': commute_time,
        'living_status': living_status
    })

    # Generate parent attributes
    parent_income = weighted_choice(range(200000, 600001), [0.03] * 200001 + [0.97] * 400001)  # 97% between 400k and 600k
    parents.append({
        'parent_id': student_id,  # Use student_id as parent_id for simplicity
        'parent_income': parent_income,
        'mother_job': fake.job(),
        'father_job': fake.job(),
    })

    # Generate teacher attributes
    teachers.append({
        'teacher_id': student_id,  # Use student_id as teacher_id for simplicity
        'qualification': random.choice(['NCE', 'B.Ed', 'M.Ed', 'PhD']),
        'experience_years': random.randint(1, 20),
        'subject_specialization': random.choice(['Mathematics', 'Science', 'Literature', 'History'])
    })

    # Generate school facilities
    school_facilities.append({
        'facility_id': student_id,  # Use student_id as facility_id for simplicity
        'facility_name': random.choice(['Library', 'Science Lab', 'Sports Ground', 'Computer Lab']),
        'availability': random.choice(['Yes', 'No']),
        'condition': random.choice(['Good', 'Average', 'Poor'])
    })

    # Generate performance data
    performance_score = weighted_choice(range(125, 224), [0.01] * 100 + [0.99] * 99)  # 1% between 195 and 223
    performances.append({
        'performance_id': student_id,  # Use student_id as performance_id for simplicity
        'exam_score': performance_score,
    })

# Create DataFrames for each entity
students_df = pd.DataFrame(students)
parents_df = pd.DataFrame(parents)
teachers_df = pd.DataFrame(teachers)
school_facilities_df = pd.DataFrame(school_facilities)
performances_df = pd.DataFrame(performances)

# Save DataFrames to CSV
students_df.to_csv('students.csv', index=False)
parents_df.to_csv('parents.csv', index=False)
teachers_df.to_csv('teachers.csv', index=False)
school_facilities_df.to_csv('school_facilities.csv', index=False)
performances_df.to_csv('performances.csv', index=False)

print("CSV files generated successfully!")
