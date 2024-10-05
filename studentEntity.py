from faker import Faker
import pandas as pd
import random

# Initialize Faker object for Nigeria (en_NG locale)
fake = Faker('en_NG')

# Number of records to generate
num_students = 400

# Expanded custom Yoruba names (150 samples)
sample_first_names = [
    'Adebayo', 'Ayotunde', 'Folake', 'Oluwatobi', 'Bamidele', 'Kehinde', 'Temidayo', 'Iretiola', 'Funke', 'Gbenga',
    'Adetokunbo', 'Bola', 'Demilade', 'Folusho', 'Modupe', 'Yetunde', 'Oluwaseyi', 'Omotola', 'Taiwo', 'Seyi',
    'Titi', 'Wuraola', 'Olamide', 'Seun', 'Adeola', 'Morounke', 'Titilayo', 'Boluwatife', 'Adekunle', 'Akin',
    'Bunmi', 'Durojaiye', 'Ibukun', 'Ismail', 'Kolawole', 'Kunle', 'Lekan', 'Mojisola', 'Odunayo', 'Opeyemi',
    'Segun', 'Shola', 'Sola', 'Tade', 'Tayo', 'Tope', 'Yewande', 'Fisayo', 'Adeyemi', 'Oluwapelumi', 'Ayomide',
    'Ebunoluwa', 'Adesola', 'Tiwalade', 'Korede', 'Sunkanmi', 'Oyinlola', 'Anuoluwapo', 'Ayoola', 'Ayodeji', 'Olumide',
    # Continue with more Yoruba names...
    'Adewale', 'Ademola', 'Folarin', 'Omotayo', 'Tomiwa', 'Tobiloba', 'Olujimi', 'Oluwakemi', 'Adebisi', 'Opeyemi',
    'Idowu', 'Oreoluwa', 'Jibola', 'Tomi', 'Temiloluwa', 'Olalekan', 'Bolaji', 'Oluwole', 'Oluwafemi', 'Kikelomo',
    'Moyinoluwa', 'Oluwadamilola', 'Omowumi', 'Adedayo', 'Oluwafunmilayo', 'Olawunmi', 'Adebimpe', 'Ademolu', 'Akintunde',
    'Oluwabunmi', 'Folashade', 'Oluwasunmisola', 'Ayobami', 'Abisoye', 'Olayinka', 'Adeyinka', 'Aderemi', 'Oluwakunmi',
    # 150 Yoruba names here
]

sample_last_names = [
    'Olawale', 'Akinyemi', 'Fasola', 'Adesanya', 'Adebisi', 'Ogunleye', 'Akinsola', 'Fagbemi', 'Soyinka', 'Oyelowo',
    'Adebanjo', 'Aderibigbe', 'Ajayi', 'Akande', 'Adebayo', 'Alade', 'Awolowo', 'Bakare', 'Balogun', 'Daramola',
    'Elegbede', 'Eshinlokun', 'Fadeyi', 'Fajuyi', 'Ige', 'Ilesanmi', 'Ogunremi', 'Ogunjimi', 'Ogunbiyi', 'Oluwole',
    'Olajide', 'Olaniyi', 'Olanrewaju', 'Olapade', 'Olumuyiwa', 'Omorege', 'Oni', 'Onwudiwe', 'Osinbajo', 'Otubusin',
    'Owolabi', 'Oyebode', 'Oyeleke', 'Afolabi', 'Aladejebi', 'Awoniyi', 'Awe', 'Babatunde', 'Bamigboye', 'Bankole',
    # Continue with more Yoruba last names...
    'Gbadebo', 'Ibiyemi', 'Ladejobi', 'Obafemi', 'Odutola', 'Ogunmodede', 'Ojikutu', 'Okusanya', 'Onashile', 'Oni',
    'Orekoya', 'Oyinlola', 'Oyewole', 'Oyetunji', 'Adebowale', 'Adejumobi', 'Adeniyi', 'Adetola', 'Adetoye', 'Adetunji',
    'Adewumi', 'Ajibola', 'Ajimobi', 'Ajisafe', 'Akintola', 'Akintoye', 'Akinwande', 'Anjorin', 'Aribisala', 'Awe',
    'Babajide', 'Balogun', 'Durojaiye', 'Esan', 'Fadipe', 'Fashola', 'Gbadamosi', 'Ibikunle', 'Ilori', 'Imole',
    # 150 Yoruba last names here
]

# Sample states
sample_states = ['Lagos', 'Oyo', 'Ogun', 'Osun']

# List to store generated student data
student_data = []

# Generate student data based on Yoruba names and specific states
for i in range(num_students):
    student_id = fake.unique.random_number(digits=5, fix_len=True)
    
    student_data.append({
        'student_id': student_id,
        'first_name': random.choice(sample_first_names),  # First name from Yoruba pool
        'last_name': random.choice(sample_last_names),    # Last name from Yoruba pool
        'gender': random.choice(['Male', 'Female']),      # Random gender
        'date_of_birth': fake.date_of_birth(minimum_age=15, maximum_age=20),
        'class': random.choice(['SS1', 'SS2', 'SS3']),
        'address': fake.street_address(),
        'city': fake.city(),
        'state': random.choice(sample_states),            # State from predefined list
        'country': 'Nigeria',
        'enrollment_date': fake.date_this_decade()
    })

# Convert to DataFrame and save as CSV
df_students = pd.DataFrame(student_data)
df_students.to_csv('students.csv', index=False)

print("Student dataset with 400 records saved as 'students.csv'.")
