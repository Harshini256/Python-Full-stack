'''
Input() --> input formatting
print() --> output formatting (fstring)

a,b = 13,4.5
print(a, b)
print(a,b,sep=',')
print(9,20,sep=':')
print('codegnan','python','vizag',sep='---->')

#end by throws new line,we can modify it ...
print(a,b,end=' ')
print('codegnan is in vizag',end='\t')
print('pfs6 and da6')
print('---- welcome to the game ----')

#use print() and build a simple calculator application
#ask inputs from user-->add,subtract,multiply and divide

#a,b = map(int,input('enter a values: ').split(','))
#print(a+b,end=' ')
#print(a-b)
#print(a*b,end=' ')
#print(a/b)


#usage of %d,%f,%s -->prefer this type only when ur working on calculations
#print('usage of %'%(args))
price = 45.5;grade='A';stock=15
print('%d'%price)
#print('%d'%grade) -->type error
print('price is %d'%price)

print('price is %f'%price)
print('price is %.1f'%price)
print()
print('grade is %s'%grade)
print()
print('stock is %d'%stock)
print('stock is %f'%stock)


#area of circle when radius is 3.5 cm,round of the area to 2 decimal values.
#take pi value as 3.1416


pi = 3.1416
r = 3.5
area = pi *(r **2)
print(area)
print('area of circle is %.2f'%area)


#new style formatting --> fstring

name = 'codegnan';batch ='pfs6'
print(f'{batch}is in{name}')
print(f'harshini is in {name} from {batch}')


#control block statements: -->they control the flow of the program
#they are 3 types -->1.conditional statements(if,elif,else),
#                    2.repetitive statements (loops --> for,while)
#                    3.jumping statements(break,continue,pass)



syntax for conditional statements:

if condition syntax:

if <condition>:
    statements(s)...
    .....
    ...
elif <conditions>:
     statement(s) ...
     .....
else:
    statement(s)...
    .....


#BMI converter(body mass index) -->weight,ks,cm
#height -->feets -->1 feet --> 12 inches --> 1 inch --> 2.54 cm
#BMI = weight/((height)**2)

weight = int(input('enter weight in kgs'))
height = float(input('enter the height in metres:'))
name = input('enter the name: ')
bmi = weight / ((height)**2)
print(bmi)

#lets divide into categories


<18.5 --> under weight
>= 18.5 - 24.9 -->healthy
>=25 - 29.9 -->over weight
>30 -->obesity


if weight > 0 and height > 0:
    bmi = weight / ((height)**2)
if bmi<18.5:
    print(f'bmi of {name} is {bmi} and you are underweight')
elif bmi>18.5 and bmi<24.9:
    print(f'bmi of {name} is {bmi} and you are Healthy --> keep consistent')
elif bmi>=25 and bmi<=29.9:
    print(f'bmi of {name} is {bmi} and you are Overweight -->\start exercising')
elif bmi>30:
    print(f'{name} is in obase category and bmi is {bmi}')
else:
    print('do enter only positive values greater than 0')

'''
#task --> user can enter height in centimeters, feets ---> meters(calculate bmi)
#make all user validations for height --> cms,feets.
#post link in git hub.

weight = int(input('enter weight in kgs'))
choice = int(input('enter any choice \n1.centimeter \n2.meters \n3.feet:'))
height = float(input('enter your height'))
if choice ==1:
    height = height/100
elif choice ==2:
    height=height
elif choice ==3:
    height=height*0.3070
name = input('enter your name: ')
bmi = weight / ((height)**2)

if bmi<18.5:
    print(f'bmi of {name} is {bmi} and you are underweight')
elif bmi>18.5 and bmi<24.9:
    print(f'bmi of {name} is {bmi} and you are Healthy --> keep consistent')
elif bmi>=25 and bmi<=29.9:
    print(f'bmi of {name} is {bmi} and you are Overweight -->\start exercising')
elif bmi>30:
    print(f'{name} is in obase category and bmi is {bmi}')
else:
    print('do enter only positive values greater than 0')

    









    




