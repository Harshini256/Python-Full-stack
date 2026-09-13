# ATM - AUTOMATED TELLER MACHINE

harshini_details_SBI = {
    'Name' : 'Harshini',
    'Adr'  : '551396662503',
    'Pan'  : 'GPCBU2073T',
    'ATMPIN' :input('set pin: '),
    'Balance': 20000,
    'Mini Statement':[]
}
all_attmps = 3
while all_attmps > 0:
    user_pin = input('Enter your atm pin: ')
    if user_pin in harshini_details_SBI['ATMPIN'] and len(user_pin) ==4:
        print('Welcome to SBI ATM')
        choice_ = int(input('Enter \n1.Withdraw \n2.Deposit \n3.Check Balance \n4.Change Pin: '))
        if choice_ == 1:
            withdraw_amount = int(input('Enter amount to Withdraw: '))
            if withdraw_amount <= harshini_details_SBI['Balance'] and withdraw_amount % 100 == 0:
                harshini_details_SBI['Balance'] -= withdraw_amount
                print(f'Take your cash and the balance is {harshini_details_SBI['Balance']}')
                harshini_details_SBI['Mini Statement'].append(f'withdraw: {withdraw_amount}')
                print(f'{harshini_details_SBI['Mini Statement']}')
                user_opt = int(input('Enter \n1.Home Page \n2.Exit page: '))
                if user_opt ==1:
                    print('Taking to home page')
                elif user_opt ==2:
                     print('Thanks for visiting')
                     break
                               
            else:
                print('Insufficient balance or This ATM cannot provide change')
                break
        elif choice_ == 2:
            deposit_amount = int(input('Enter amount to deposit: '))
            if deposit_amount % 100 ==0:
                harshini_details_SBI['Balance'] += deposit_amount
                print(f'amount to deposit and total amount in {harshini_details_SBI['Balance']}')
                harshini_details_SBI['Mini Statement'].append(f'deposit: {deposit_amount}')
                print(f'{harshini_details_SBI['Mini Statement']}')
                user_opt = int(input('Enter \n1.Home Page \n2.Exit page: '))
                if user_opt ==1:
                    print('Taking to home page')
                elif user_opt ==2:
                     print('Thanks for visiting')
                     break
            else:
                print('This ATM is not accepts change')
        elif choice_ == 3:
            balance_check = input('Do you want to check your balance? (y/n): ')
            if balance_check.lower() == 'y':
                print(f'Your  total balance is {harshini_details_SBI['Balance']}')
            else:
                print('Thank you for using SBI ATM')
        elif choice_ == 4:
            old_pin = input('Enter your old pin: ')
            if old_pin == harshini_details_SBI['ATMPIN']:
                new_pin = input('Enter your new pin: ')
                harshini_details_SBI['ATMPIN'] = new_pin
                print('Your pin has been changed successfully')
            else:
                print('Incorrect pin.failed to change pin')
    else:
        all_attmps -= 1
        if all_attmps > 0:
            print(f'Incorrect pin entered and you have{all_attmps} left')
        else:
            print('Your Card is Blocked...')

            
