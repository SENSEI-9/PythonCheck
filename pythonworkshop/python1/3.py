#N students take K apples and distribute them among each other evenly.
# The remaining(the undivisible) part remains in the basket. How many apples will remain in the basket?
# The program reads the numbers N and K. it should print the two answers for the questions above.
no_of_students=int(input('enter the number of students'))
no_of_apples=int(input('enter the number of apples'))
basket=no_of_apples//no_of_students
in_basket=no_of_apples%no_of_students
print('distributed apples to each student',basket)
print('remaining apples in basket',in_basket)