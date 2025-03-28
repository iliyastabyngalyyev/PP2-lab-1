class Human:
    def __init__(self, name, familyname, age, gender, nationality):
        self.name = name
        self.familyname = familyname
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def set_name(self, name):
        self.name = name

    def set_family(self, familyname):
        self.familyname = familyname

    def set_age(self, age):
        self.age = age

    def set_gender(self, gender):
        self.gender = gender

    def set_nationality(self, nationality):
        self.nationality = nationality

    def Get_info(self):
        return {
            "name": self.name,
            "familyname": self.familyname,
            "age": self.age,
            "gender": self.gender,
            "nationality": self.nationality
        }

class Student(Human):
    def __init__(self, name, familyname, age, gender, nationality, school=None):
        super().__init__(name, familyname, age, gender, nationality)
        self.school = school
        self.subjects = []

    def set_school(self, school):
        self.school = school

    def Add_Subject(self, subject):
        self.subjects.append(subject)

class Teacher(Human):
    def __init__(self, name, familyname, age, gender, nationality, school=None):
        super().__init__(name, familyname, age, gender, nationality)
        self.school = school
        self.subject = None

    def set_school(self, school):
        self.school = school

    def Add_Subject(self, subject):
        self.subject = subject

if __name__ == "__main__":
    print("users модулі сәтті импортталды.")
    print("Сыныптар: Human, Student, Teacher")
    print("Әдістер: set_name, set_family, set_age, set_gender, set_nationality, Get_info, set_school, Add_Subject")
