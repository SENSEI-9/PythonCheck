'''5. A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks that
can be purchased.The program should read three integers: the number of students in each of the
 three classes,a,b and c respectively.
In the first test are three group. The first group has 20 students and thus needs 10 desks. The
second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also
enough for the third group of 22 students. So, we need 32 desks in total.'''

no_students_class1=int(input('enter the number of students in first class: '))
no_student_class2=int(input('enter the number of students in second class: '))
no_student_class3=int(input('enter the number of students in third class: '))
desk_in_class1=(no_students_class1//2)
remaining_desks1=(no_students_class1%2)
total_desks_required1=desk_in_class1+remaining_desks1
print('the total no of desk in first class is',total_desks_required1)
desk_in_class2=(no_student_class2//2)
remaining_desks2=(no_student_class2%2)
total_desks_required2=desk_in_class2+remaining_desks2
print('the total no of desk in second class is',total_desks_required2)
desk_in_class3=(no_student_class3//2)
remaining_desks3=(no_student_class3%2)
total_desks_required3=(desk_in_class3+remaining_desks3)
print('the total no of desk required in class 3 is', total_desks_required3)
total_students=no_students_class1+no_student_class2+no_student_class3
print('the total no of student is',total_students)
total_desks=(total_desks_required1+total_desks_required2+total_desks_required3)
print('the total desks are',total_desks)
