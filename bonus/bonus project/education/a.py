import users
import organizations

s1 = users.Student("Айша", "Бекенова", 16, "әйел", "Қазақ")
s1.set_school("Жуз 40 мектебі")
s1.Add_Subject("Математика")
s1.Add_Subject("Физика")

s2 = users.Student("Бекжан", "Алиев", 17, "ер", "Қазақ")
s2.set_school("Жуз 40 мектебі")
s2.Add_Subject("Тарих")
s2.Add_Subject("Әдебиет")

s3 = users.Student("Ержан", "Кенесов", 15, "ер", "Қазақ")
s3.set_school("Шамшырак мектебі")
s3.Add_Subject("Химия")
s3.Add_Subject("Биология")

s4 = users.Student("Мадина", "Серікбаева", 16, "әйел", "Қазақ")
s4.set_school("Шамшырак мектебі")
s4.Add_Subject("Ағылшын тілі")
s4.Add_Subject("Физика")

s5 = users.Student("Нұржан", "Әбдірахманов", 17, "ер", "Қазақ")
s5.set_school("Каз билим лицейі")
s5.Add_Subject("Информатика")
s5.Add_Subject("География")

s6 = users.Student("Әсел", "Омарова", 16, "әйел", "Қазақ")
s6.set_school("Каз билим лицейі")
s6.Add_Subject("Химия")
s6.Add_Subject("Физика")

t1 = users.Teacher("Мырзағали", "Жұмабаев", 45, "ер", "Қазақ")
t1.set_school("Жуз 40 мектебі")
t1.Add_Subject("Математика")

t2 = users.Teacher("Анар", "Сейітова", 40, "әйел", "Қазақ")
t2.set_school("Жуз 40 мектебі")
t2.Add_Subject("Тарих")

t3 = users.Teacher("Самат", "Нұрғалиев", 38, "ер", "Қазақ")
t3.set_school("Шамшырак мектебі")
t3.Add_Subject("Химия")

t4 = users.Teacher("Гүлнар", "Қасымова", 42, "әйел", "Қазақ")
t4.set_school("Шамшырак мектебі")
t4.Add_Subject("Физика")

t5 = users.Teacher("Жанар", "Мұратова", 37, "әйел", "Қазақ")
t5.set_school("Каз билим лицейі")
t5.Add_Subject("Информатика")

t6 = users.Teacher("Қанат", "Ермеков", 44, "ер", "Қазақ")
t6.set_school("Каз билим лицейі")
t6.Add_Subject("Химия")

school1 = organizations.School("Жуз 40 мектебі", "Алматы, Қазақстан", "87056576588", "contact@juz40.kz", 5000, 100)
school1.add_student(s1)
school1.add_student(s2)
school1.add_teacher(t1)
school1.add_teacher(t2)

school2 = organizations.School("Шамшырак мектебі", "Актау, Қазақстан", "87077521244", "contact@sham.kz", 750, 55)
school2.add_student(s3)
school2.add_student(s4)
school2.add_teacher(t3)
school2.add_teacher(t4)

school3 = organizations.School("Каз билим лицейі", "Шымкент, Қазақстан", "87052059742", "contact@QZbilim.kz", 600, 40)
school3.add_student(s5)
school3.add_student(s6)
school3.add_teacher(t5)
school3.add_teacher(t6)

print(school1.Get_info())
print(school2.Get_info())
print(school3.Get_info())

school1.Get_Report("juz_40_report.csv")
school2.Get_Report("Shamshyrak_report.csv")
school3.Get_Report("Qaz_Bilim_report.csv")