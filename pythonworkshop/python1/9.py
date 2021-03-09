'''write a program to take input from the user, Ask the users age. If the user age is
below 15 print a message "you are a child", if the users age is greater than 15 and lesser than
40 print "you are a adult" a message if the user age is greater than 40 print "you are old" '''
age=int(input('Enter your age'))
if age<=15:
    print('you are a child')
elif age>15 and age<=40:
    print('you are a adult')
elif age<40:
    print('you are old')
