'''
#Students Marks File Manager:

with open('marks.txt', 'w')as file:
    for i in range(5):
        try:
            marks = int(input('Enter student mark: '))
            if marks<=100 and marks>0:
                file.write(str(marks) + '\n')
                print('Mark saved successfully!')
            else:
                print('Invalid marks: ')
        except ValueError:
             print('please enter a Valid marks')
        except Exception as e:
            print(e)
print('\nSaved Marks:')
with open('marks.txt', 'r')as file:
    for mark in file:
        print(mark.strip())



#Expense Tracker:

with open('expenses.txt', 'w')as file:
    for i in range(5):
        try:
            expenses = float(input('Enter expenses amount:'))
            if expenses>0:
                file.write(str(expenses) + '\n')
            else:
                print('Invalid Expense data')
        except ValueError:
            print('Invalid expense data')
print('\nSaved Expenses: ')
total = 0
try:
    with open('expenses.txt', 'r')as file:
        for expenses in file:
            amount = float(expenses.strip())
            total = total+amount
            print(amount)
        print(f'Total expense: {total}')
except FileNotFoundError:
    print('File doesnot exist')



#Student Attendance Manager:


with open('attendance.txt', 'w')as file:
    for i in range (5):
        try:
            students = input('Enter student name: ')
            status = input('Enter attendance status(P/A): ')
            if status == 'P':
                print('It is valid status')
                file.write(students + ',' + status + '\n')

            elif status == 'A':
                print('It is invalid ')
                file.write(students + ',' + status + '\n')

            else:
                print('Invalid attendance status')
                
        except exception as e:
            print('unexpected input-related error', e)
print('\nPresent Students: ')
try:
    with open('attendance.txt', 'r')as file:
        for record in file:
            name, status = record.strip().split(',')
            if status == 'P':
                print(name)
except FileNotFoundError:
    print('Attendance file doesnot exist')

'''
#Product Inventory Manager:

'''with open('inventory.txt', 'a')as file:
    for i in range(3):
        try:
            
            products = input('Enter Product name: ')
            quantity = int(input('Enter a number:  '))
            if quantity >= 0:
                file.write(products+ "-" +str(quantity)+ "\n")
        except ValueError:
            print("please enter a valid integer.")'''
print('\nCurrent Inventory: ')
try:
    with open('inventory.txt','r')as file:
        for product in file:
            print(product.strip())
    search_product = input('Enter product name to search: ')
    with open('inventory.txt', 'r') as file:
        #found = False
        products = {}
        for product in file:
            product = product.strip().split("-")
            products['product_name'] = product[0]
            products['quantity'] = int(product[1])  
            #print(products)
            if search_product in products['product_name']:
                #print(product)
                print(f'{search_product} is available.')
                print(f'Quantity : {products["quantity"]}')
                break
        else:
            print("Product not found.")
except FileNotFoundError:
    print('File doesnot exisist')

            
            
            
            
                
            
            
        


            
            




    
    
            
            
        
    
