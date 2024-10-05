import pandas as pd
import random
from faker import Faker

fake = Faker('en_NG')  # Nigeria-specific locale
Faker.seed(42)

# 150 Yoruba first and last names (sample from earlier code)
sample_first_names = [
    'Adebayo', 'Ayotunde', 'Folake', 'Oluwatobi', 'Bamidele', 'Kehinde', 'Temidayo', 'Iretiola', 
    'Funke', 'Gbenga', 'Adedayo', 'Olufemi', 'Oluwaseun', 'Bola', 'Yetunde', 'Damilola', 
    'Oluwakemi', 'Sola', 'Omotola', 'Olajide', 'Adeniyi', 'Olumide', 'Boluwatife', 'Adeola', 
    'Titilayo', 'Oluwadamilare', 'Adekunle', 'Abimbola', 'Ayodele', 'Segun', 'Tayo', 
    'Olawale', 'Mobolaji', 'Omowunmi', 'Oluwanifemi', 'Fiyinfoluwa', 'Ajibola', 'Tolulope', 
    'Adetola', 'Opeoluwa', 'Adenike', 'Ayomide', 'Babajide', 'Morenike', 'Olujimi', 'Kikelomo', 
    'Opeyemi', 'Adeyinka', 'Anuoluwapo', 'Oluwatoyin', 'Tunde', 'Oluwole', 'Ibitoye', 'Gbolahan', 
    'Demilade', 'Oluwadamilola', 'Babatunde', 'Tiwalade', 'Erioluwa', 'Mayowa', 'Oluwanifemi', 
    'Olushola', 'Ademola', 'Oreoluwa', 'Oluwapelumi', 'Ifeoluwa', 'Olamide', 'Olayinka', 
    'Oluwakayode', 'Taiwo', 'Tope', 'Oluwatobi', 'Funmilayo', 'Oluwole', 'Adebimpe', 'Tobiloba', 
    'Yewande', 'Afolabi', 'Adunni', 'Oluwafemi', 'Adetayo', 'Adeyemi', 'Adesola', 'Oluwakemi', 
    'Oreofe', 'Oluwadare', 'Ifedayo', 'Ajoke', 'Abiodun', 'Olatunde', 'Oluwashina', 'Oluwadamilola',
    'Aderonke', 'Oluwadara', 'Oluwakunle', 'Titilope', 'Folusho', 'Adejoke', 'Aderemi', 'Oluwasola', 
    'Mofoluwake', 'Oluwasemilore', 'Olufolake', 'Olamiposi', 'Oluwatimilehin', 'Adunola', 
    'Olufisayo', 'Adeola', 'Oluwatobi', 'Oluwadamilola', 'Oladimeji', 'Adenike', 'Adeniran', 
    'Olumuyiwa', 'Iretiola', 'Boluwaji', 'Oluwadunsin', 'Oluwasegun', 'Oluwakorede', 'Oladayo', 
    'Mofeoluwa', 'Oluwatosin', 'Oluwole', 'Akinola', 'Oluwadamilare', 'Adeniran', 'Akinbode',
    'Opeyemi', 'Oluwafunmilayo', 'Olubunmi', 'Folarin', 'Tosin', 'Adeniran', 'Toluwalase', 
    'Olatunde', 'Oluwanishola'
]

sample_last_names = [
    'Olawale', 'Akinyemi', 'Fasola', 'Adesanya', 'Adebisi', 'Ogunleye', 'Akinsola', 'Fagbemi', 
    'Soyinka', 'Oyelowo', 'Adebanjo', 'Adefemi', 'Ajayi', 'Awolowo', 'Oshodi', 'Babalola', 'Oniru', 
    'Ogundele', 'Odetola', 'Akinlade', 'Egunjobi', 'Osunbade', 'Salako', 'Ibrahim', 'Adedeji', 
    'Akinola', 'Olatunji', 'Olubode', 'Olowookere', 'Oladokun', 'Aderibigbe', 'Omodara', 'Salami', 
    'Fadeyi', 'Ajagbe', 'Aderemi', 'Ogunlana', 'Olatoye', 'Ogbemudia', 'Adepoju', 'Ogunbiyi', 
    'Alade', 'Olokun', 'Adegunle', 'Olanipekun', 'Adetunji', 'Adekanbi', 'Balogun', 'Obafemi', 
    'Ajiboye', 'Adelabu', 'Adeniran', 'Olumide', 'Adediran', 'Akinyemi', 'Oyekanmi', 'Odugbemi', 
    'Adebayo', 'Olajide', 'Oladimeji', 'Olagunju', 'Ogunsanya', 'Okanlawon', 'Olaniyan', 
    'Oladimeji', 'Ogundipe', 'Onasanya', 'Adeboye', 'Akinyemi', 'Odusanya', 'Onibudo', 'Arowolo', 
    'Olanipekun', 'Adebiyi', 'Olusola', 'Ogunfemi', 'Aina', 'Adeola', 'Olufemi', 'Ajibola', 'Akingbade', 
    'Olubode', 'Osunwole', 'Olubodun', 'Olufon', 'Adeola', 'Ajayi', 'Ogunwale', 'Olaoluwa', 
    'Adeoye', 'Akinfemi', 'Akintunde', 'Akinbode', 'Ajayi', 'Adeyemo', 'Akintola', 'Alimi', 
    'Akanni', 'Adebajo', 'Awolola', 'Akinlotan', 'Oladele', 'Adebayo', 'Ogunbi', 'Olugbemi', 
    'Olufon', 'Olumide', 'Adebiyi', 'Ogunrinade', 'Olufon', 'Adedokun', 'Olusola', 'Adeyeye', 
    'Olufunke', 'Oyekunle', 'Odukoya', 'Adewunmi', 'Onajobi', 'Ogundipe', 'Olatunbosun', 
    'Onabanjo', 'Osinbajo', 'Adebimpe', 'Adedeji', 'Ogundipe', 'Akinbobola', 'Ajiboye', 
    'Adesuyi', 'Akinfenwa', 'Oduwole', 'Ajibola', 'Oluwabiyi', 'Adewusi', 'Adebajo'
]

sample_states = ['Lagos', 'Oyo', 'Ogun', 'Osun']

# Function to generate student data
def generate_student_data(num_records=400):
    student_data = []
    for i in range(1, num_records + 1):
        first_name = random.choice(sample_first_names)
        last_name = random.choice(sample_last_names)
        state = random.choice(sample_states)
        age = random.randint(16, 21)
        gender = random.choice(['Male', 'Female'])
        student_data.append([i, first_name, last_name, age, gender, state])
    return student_data

# Function to generate parent data
def generate_parent_data(student_data):
    parent_data = []
    for student in student_data:
        parent_income = random.randint(500000, 2000000)
        parent_education_level = random.choice(['High School', 'Bachelor\'s Degree', 'Master\'s Degree', 'PhD'])
        parent_data.append([student[0], fake.name(), parent_income, parent_education_level])
    return parent_data

# Function to generate library usage data
def generate_library_usage(student_data):
    library_usage = []
    for student in student_data:
        hours_spent = random.uniform(5, 8)
        books_read = random.randint(6, 9)
        library_usage.append([student[0], round(hours_spent, 2), books_read])
    return library_usage

# Function to generate extra-curricular activity data
def generate_extra_curricular(student_data):
    extra_curricular = []
    activities = ['Sport', 'Drama', 'Music', 'Debate']
    for student in student_data:
        activity = random.choice(activities)
        extra_curricular.append([student[0], activity])
    return extra_curricular

# Function to generate performance data
def generate_performance_data(student_data):
    performance_data = []
    for student in student_data:
        exam_type = 'JAMB'
        score = random.choices([random.randint(300, 335), random.randint(245, 299)], weights=[5, 95])[0]
        performance_data.append([student[0], exam_type, score])
    return performance_data

# Generate data
students = generate_student_data()
parents = generate_parent_data(students)
library_usage = generate_library_usage(students)
extra_curricular = generate_extra_curricular(students)
performance = generate_performance_data(students)

# Convert to DataFrames
students_df = pd.DataFrame(students, columns=['Student ID', 'First Name', 'Last Name', 'Age', 'Gender', 'State'])
parents_df = pd.DataFrame(parents, columns=['Student ID', 'Parent Name', 'Parent Income', 'Parent Education Level'])
library_usage_df = pd.DataFrame(library_usage, columns=['Student ID', 'Hours Spent in Library', 'Books Read'])
extra_curricular_df = pd.DataFrame(extra_curricular, columns=['Student ID', 'Extra Curricular Activity'])
performance_df = pd.DataFrame(performance, columns=['Student ID', 'Exam Type', 'Score'])

# Save to CSV
students_df.to_csv('students_data.csv', index=False)
parents_df.to_csv('parents_data.csv', index=False)
library_usage_df.to_csv('library_usage.csv', index=False)
extra_curricular_df.to_csv('extra_curricular.csv', index=False)
performance_df.to_csv('performance_data.csv', index=False)

print("Data generation completed and saved as CSV files.")
