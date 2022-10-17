from random import randint
print("")

spisok_imen = ["Emily Hannah Kaitlyn Sarah Madison Brianna Kaylee Hailey Alexis Elizabeth Taylo Lauren Ashley Katherine Jessica Anna Samantha lissa Kayla"]
delimiter = " "
spisok_imen = delimiter.join(spisok_imen)
spisok_imen = spisok_imen.split(delimiter)

group_1 = []
group_2 = []
group_3 = []
Number_of_students = 20
Number_of_names = len(spisok_imen)
count_teska = 0
group_bez_tesok = []
group_s_teskami = []


for i in range(Number_of_students):
    sequence_number_name = randint(0,Number_of_names-1)
    group_1.append(spisok_imen[sequence_number_name])

    sequence_number_name = randint(0, Number_of_names - 1)
    group_2.append(spisok_imen[sequence_number_name])

    sequence_number_name = randint(0, Number_of_names - 1)
    group_3.append(spisok_imen[sequence_number_name])

print("Первая группа",group_1)
print("Вторая группа",group_2)
print("Третья группа",group_3)


for qew in range(Number_of_students):
    name_student = group_1[qew]
    count_teska = group_2.count(group_1[qew]) + group_3.count(group_1[qew])
    if count_teska == 0:
        group_bez_tesok.append(name_student)
    count_teska = group_2.count(group_1[qew]) * group_3.count(group_1[qew])
    if count_teska > 0:
        group_s_teskami.append(name_student)

    name_student = group_2[qew]
    count_teska = group_1.count(group_1[qew]) + group_3.count(group_1[qew])
    if count_teska == 0:
        group_bez_tesok.append(name_student)

    name_student = group_3[qew]
    count_teska = group_1.count(group_1[qew]) + group_2.count(group_1[qew])
    if count_teska == 0:
        group_bez_tesok.append(name_student)


print(" ")
print("Студенты с тесками:  ",group_s_teskami)
print("Студенты без тесок:  ",group_bez_tesok)
