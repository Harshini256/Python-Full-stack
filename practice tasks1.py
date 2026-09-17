#GRADE CHECKER

marks = int(input('Enter your marks: '))
name = input('Enter ur name: ')
grade1 = 'A'
grade2 = 'B'
grade3 = 'C'
grade4 = 'D'
grade5 = 'E'
grade6 = 'F'
if marks<0 or marks >100:
    print('Invalid marks entered')
elif marks >= 90:
    print(f'{name} your grade is "{grade1}" and  you have remarks as "Outstanding!"')
elif marks >= 80:
    print(f'{name} your grade is "{grade2}" and  you have remarks as "Excellent!"')
elif marks >=70:
    print(f'{name} your grade is "{grade3}" and  you have remarks as "Good"')
elif marks >=60:
    print(f'{name} your grade is "{grade4}" and  you have remarks as "Fair,needs improvement"')
elif marks >=50:
    print(f'{name} your grade is "{grade5}" and  you have remarks as "Poor,needs serious improvement"')
else:
    print(f'{name} your grade is "{grade6}" and  you are "Failed,needs to reappear"')



#Even-Odd Checker:

try:
    number = int(input('Enter a number: '))
    if number == 0:
        print('Zero is neither even nor odd')
    elif number < 0 and number %2 == 0:
        print('Negative Even Number')
    elif number < 0 and number %2 != 0:
        print('Negative Odd Number')
    elif number > 0 and number %2 == 0:
        print('Even Number')
    else:
        print('Odd Number')
except ValueError:
    print('please enter the code correctly with only the type of integers')
except Exception as e:
    print(e)
finally:
    print('Executed Successfully1')


#Season Identifier:

season = int(input('Enter a month: '))
if season >=12:
    print('Invalid month you entered')
elif season == 12 or season == 1 or season == 2:
    print('It is "Winter" Season')
elif season == 3 or season == 4 or season == 5:
    print('It is "Spring" Season')
elif season == 6 or season == 7 or season == 8:
    print('It is "Summer" Season')
elif season == 9 or season == 10 or season == 11:
    print('It is Autumn Season')
else:
    print('Invalid')


    

    
