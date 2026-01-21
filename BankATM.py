balance = 100

print('ATM')
print('-----')
print('1. Withdraw')
print('2. Deposit')
print('3. View Balance')

user_input = int(input('>Enter option: '))

if user_input == 1:
    amount = float(input('Enter amount: $'))
    balance = balance - amount
    print(f'New balance: ${balance}')
elif user_input == 2:
    amount = float(input('Enter amount: $'))
    balance = balance + amount
    print(f'New balance: ${balance}')
elif user_input == 3:
    print(f'Your balance is: ${balance}')
else:
    print('Invalid option')