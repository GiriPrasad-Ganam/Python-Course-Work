data = {
    12345:{'pin':1234, 'balance':5000, 'transaction':[]},
    12346:{'pin':1234, 'balance':6000, 'transaction':[]},
    12347:{'pin':1234, 'balance':7000, 'transaction':[]},
    12348:{'pin':1234, 'balance':8000, 'transaction':[]}
}


# login page logic
def login():
    global acc_num
    acc_num = int(input('Enter Account Number: '))
    pin = int(input('Enter pin number: '))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print('Login successfully')
        return True
    else:
        print('Invalid Login')
        return False

#menu page logic

def menu():
    print()
    print('[C]heckBalance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[T]ransactions')
    print('change [P]in')
    print('[E]xit')


def checkBalance():
    print(f'Current Balance is {data[acc_num]['balance']}')


def deposite():
    amount = int(input('Enter Deposite Amount: '))
    data[acc_num]['balance']+=amount
    data[acc_num]['transaction'].append(f'despoite Amount: {amount}')
    print('Deposite Successfully!')


def withdraw():
    amount = int(input('Enter withdraw Amount: '))
    if data[acc_num]['balance']>amount:
        data[acc_num]['balance']-=amount
        data[acc_num]['transaction'].append(f'withdraw Amount{amount}')
        print('Withdraw Successfully!')
    else:
        print('Insufficent Amount')

def transaction():
    if data[acc_num]['transaction']:
        print('_______________Transaction History_______________')
        for i in data[acc_num]['transaction']:
            print(i)
    else:
        print('No Transaction yet')

def changePin():
    data[acc_num]['pin']=int(input('Enter New Pin Number: '))
    print('successfully Pin number changed!')

