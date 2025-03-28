import csv

class School:
    def __init__(self, name, address, phone, email, num_stud, num_teachers):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.num_stud = num_stud
        self.num_teachers = num_teachers
        self.students = []
        self.teachers = []

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def set_num_stud(self, num_stud):
        self.num_stud = num_stud

    def set_num_teachers(self, num_teachers):
        self.num_teachers = num_teachers

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def Get_info(self):
        return {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "num_students": self.num_stud,
            "num_teachers": self.num_teachers
        }

    def Get_Report(self, filename="school_report.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["School Name", self.name])
            writer.writerow(["Address", self.address])
            writer.writerow(["Phone", self.phone])
            writer.writerow(["Email", self.email])
            writer.writerow(["Number of Students", self.num_stud])
            writer.writerow(["Number of Teachers", self.num_teachers])
            writer.writerow([])  

            writer.writerow(["Students"])
            writer.writerow(["Name", "Surname", "Age", "Gender", "Nationality", "School", "Subjects"])
            for student in self.students:
                writer.writerow([student.name, student.familyname, student.age, student.gender, student.nationality, student.school, ", ".join(student.subjects)])

            writer.writerow([])  
            writer.writerow(["Teachers"])
            writer.writerow(["Name", "Surname", "Age", "Gender", "Nationality", "School", "Subject"])
            for teacher in self.teachers:
                writer.writerow([teacher.name, teacher.familyname, teacher.age, teacher.gender, teacher.nationality, teacher.school, teacher.subject])

if __name__ == "__main__":
    print("organizations модулі сәтті импортталды.")
    print("Сынып: School")
    print("Әдістер: set_name, set_address, set_phone, set_email, set_num_stud, set_num_teachers, add_student, add_teacher, Get_info, Get_Report")
