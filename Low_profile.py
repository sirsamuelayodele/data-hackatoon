import random
import csv
from faker import Faker

# Initialize Faker
fake = Faker('en_NG')

# 150 Yoruba first names
sample_first_names = [
    'Adeola', 'Adebayo', 'Adedayo', 'Adekola', 'Adenike', 'Adeolu', 'Adesola', 'Adetola', 'Adetoun', 'Adunola', 
    'Afolabi', 'Ajibola', 'Akintunde', 'Amoke', 'Anuoluwapo', 'Aremu', 'Ayodeji', 'Ayotunde', 'Babajide', 'Babatunde', 
    'Bamidele', 'Bolaji', 'Bukola', 'Busayo', 'Durojaiye', 'Durotimi', 'Ebunoluwa', 'Eniola', 'Fadekemi', 'Fadesola', 
    'Fiyinfolu', 'Folake', 'Funmilayo', 'Funmilola', 'Gbenga', 'Ibidun', 'Ibukun', 'Ifeoluwa', 'Iretiola', 'Iyanuoluwa', 
    'Jadesola', 'Jadesola', 'Jibola', 'Kafayat', 'Kehinde', 'Kolapo', 'Kofoworola', 'Ladele', 'Laitan', 'Lamide', 
    'Lanre', 'Lara', 'Mojisola', 'Morounkeji', 'Mosope', 'Motunrayo', 'Moyosore', 'Olamide', 'Olawale', 'Olufemi', 
    'Olumide', 'Olutayo', 'Olutobi', 'Omobolanle', 'Omowunmi', 'Opeyemi', 'Oreoluwa', 'Segun', 'Seyi', 'Shola', 
    'Sijibomi', 'Sola', 'Temidayo', 'Temilade', 'Temitayo', 'Tofunmi', 'Tope', 'Tosin', 'Tunde', 'Wale', 'Yewande', 
    'Yetunde', 'Yinka', 'Yomi', 'Yemisi', 'Ajoke', 'Adewale', 'Abiodun', 'Adunni', 'Alaba', 'Ayo', 'Bamidele', 
    'Fisayo', 'Folorunsho', 'Ibrahim', 'Idowu', 'Lekan', 'Makanjuola', 'Moji', 'Moradeyo', 'Niyi', 'Olawale', 
    'Olajide', 'Olatunji', 'Oluwaseun', 'Opeyemi', 'Osaretin', 'Rotimi', 'Salewa', 'Sanmi', 'Shola', 'Sikiru', 
    'Taiwo', 'Tajudeen', 'Tomiwa', 'Victor', 'Wuraola', 'Yemi', 'Yewande', 'Zainab', 'Zainab', 'Abdul', 'Abisola', 
    'Abimbola', 'Adebola', 'Adebisi', 'Adegbite', 'Adekunle', 'Adegoke', 'Ajayi', 'Akindele', 'Alabi', 'Bola', 
    'Bose', 'Busari', 'Eniola', 'Femi', 'Fola', 'Igbinosa', 'Kola', 'Modupe', 'Muyiwa', 'Nneka', 'Obafemi', 
    'Okikiola', 'Olusegun', 'Sesan', 'Suleiman', 'Tope', 'Yusuf', 'Abisola', 'Tayo', 'Aderonke', 'Oladipo'
]

# 150 Yoruba last names
sample_last_names = [
    'Abegunde', 'Abiola', 'Adebayo', 'Adebisi', 'Adegbite', 'Adekunle', 'Adelakun', 'Adeloye', 'Adeniran', 'Adeola', 
    'Adeoti', 'Adesanya', 'Adesola', 'Adetayo', 'Adetola', 'Adetunji', 'Adewale', 'Ajayi', 'Akinbiyi', 'Akinbola', 
    'Akinlolu', 'Akinola', 'Akinpelu', 'Akinrinola', 'Akintayo', 'Akintunde', 'Akinwale', 'Akinwunmi', 'Alade', 'Aluko', 
    'Anifowose', 'Aremu', 'Awolowo', 'Babalola', 'Babatope', 'Babatunde', 'Bada', 'Badejo', 'Balogun', 'Bankole', 
    'Bello', 'Dada', 'Daramola', 'Dosunmu', 'Elegbede', 'Esho', 'Fadeyi', 'Fagbenro', 'Fagbohun', 'Fasola', 
    'Fatunmbi', 'Fayemi', 'Fowowe', 'Ibikunle', 'Ige', 'Ijaduola', 'Ijebor', 'Ilesanmi', 'Irewolede', 'Iseoluwa', 
    'Ishola', 'Jaiyeola', 'Jibola', 'Jide', 'Kadiri', 'Kehinde', 'Ladejobi', 'Laniyan', 'Lasisi', 'Lawal', 
    'Lukman', 'Mabogunje', 'Makanjuola', 'Mogaji', 'Mogbonjubola', 'Mojisola', 'Mumuni', 'Ninalowo', 'Odegbami', 
    'Ogundele', 'Ogundipe', 'Ogungbemi', 'Ogunleye', 'Ogunlola', 'Ogunsanwo', 'Ojo', 'Ojulari', 'Okanlawon', 'Okunola', 
    'Olabode', 'Oladele', 'Oladipo', 'Oladokun', 'Oladunjoye', 'Olafisoye', 'Olagoke', 'Olagunju', 'Olaniran', 'Olasupo', 
    'Olatunji', 'Olawale', 'Olayemi', 'Olayinka', 'Olayiwola', 'Olujobi', 'Olumide', 'Olusanya', 'Olutayo', 'Oni', 
    'Onifade', 'Onigbinde', 'Opeoluwa', 'Opeyemi', 'Oredein', 'Oseni', 'Osibanjo', 'Osunbade', 'Owolabi', 'Oyelowo', 
    'Sadiq', 'Salako', 'Salami', 'Sangodeyi', 'Sanusi', 'Sanyaolu', 'Sasegbon', 'Shodipo', 'Sodunke', 'Sogunro', 
    'Sokefun', 'Soyinka', 'Taiwo', 'Temidayo', 'Tijani', 'Toba', 'Yusuf'
]

sample_states = ['Lagos', 'Oyo', 'Ogun', 'Osun']

# Generate 400 student records
def generate_students(num_students):
    students = []
    for i in range(1, num_students + 1):
        student = {
            "student_id": i,
            "first_name": random.choice(sample_first_names),
            "last_name": random.choice(sample_last_names),
            "state": random.choice(sample_states),
            "dob": fake.date_of_birth(minimum_age=15, maximum_age=22),
            "gender": random.choice(["Male", "Female"])
        }
        students.append(student)
    return students

# Generate parent data (foreign key - student_id)
def generate_parents(students):
    parents = []
    for student in students:
        parent = {
            "parent_id": student["student_id"],
            "student_id": student["student_id"],
            "parent_name": fake.name(),
            "income": random.randint(30000, 60000)
        }
        parents.append(parent)
    return parents

# Generate library usage data (foreign key - student_id)
def generate_library_usage(students):
    library_usage = []
    for student in students:
        usage = {
            "usage_id": student["student_id"],
            "student_id": student["student_id"],
            "hours_spent": random.uniform(0, 1),
            "books_read": random.randint(0, 2)
        }
        library_usage.append(usage)
    return library_usage

# Generate extracurricular activity data (foreign key - student_id)
def generate_extracurricular_activities(students):
    activities = []
    for student in students:
        activity = {
            "activity_id": student["student_id"],
            "student_id": student["student_id"],
            "activity_name": "None"
        }
        activities.append(activity)
    return activities

# Generate performance data (foreign key - student_id)
def generate_performance_data(students):
    performance = []
    for student in students:
        score = random.randint(125, 223)
        # Adjust to ensure less than 3% fall between 195 and 223
        if random.random() > 0.97:
            score = random.randint(195, 223)
        performance_record = {
            "performance_id": student["student_id"],
            "student_id": student["student_id"],
            "exam_score": score
        }
        performance.append(performance_record)
    return performance

# Save data to CSV
def save_to_csv(filename, fieldnames, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Generate and save all data
students = generate_students(400)
parents = generate_parents(students)
library_usage = generate_library_usage(students)
extracurricular_activities = generate_extracurricular_activities(students)
performance_data = generate_performance_data(students)

# Save each to CSV
save_to_csv("students.csv", ["student_id", "first_name", "last_name", "state", "dob", "gender"], students)
save_to_csv("parents.csv", ["parent_id", "student_id", "parent_name", "income"], parents)
save_to_csv("library_usage.csv", ["usage_id", "student_id", "hours_spent", "books_read"], library_usage)
save_to_csv("extracurricular_activities.csv", ["activity_id", "student_id", "activity_name"], extracurricular_activities)
save_to_csv("performance_data.csv", ["performance_id", "student_id", "exam_score"], performance_data)

print("Data generation complete and saved to CSV files.")
