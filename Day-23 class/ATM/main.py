import logic as lg


if lg.login():
    print('-----Welcome To SuperATM------')
    while True:
        lg.menu()
        ch = input('Enter the Choice: ').upper()
        if ch == 'C':
            lg.checkBalance()
        elif ch == 'D':
            lg.deposite()
        elif ch == 'W':
            lg.withdraw()
        elif ch == 'T':
            lg.transaction()
        elif ch == 'P':
            lg.changePin()
        elif ch == 'E':
            print('Thank you for Visit again')
            break
else:
    print("Invalid Login, Recheck again!")



'''
Enter Account Number: 12345 
Enter pin number: 1234
Login successfully
-----Welcome To SuperATM------

[C]heckBalance
[D]eposit
[W]ithdraw
[T]ransactions
change [P]in
[E]xit
Enter the Choice: c
Current Balance is 5000

[C]heckBalance
[D]eposit
[W]ithdraw
[T]ransactions
change [P]in
[E]xit
Enter the Choice: d
Enter Deposite Amount: 2000
Deposite Successfully!

[C]heckBalance
[D]eposit
[W]ithdraw
[T]ransactions
change [P]in
[E]xit
Enter the Choice: w
Enter withdraw Amount: 1000
Withdraw Successfully!

[C]heckBalance
[D]eposit
[W]ithdraw
[T]ransactions
change [P]in
[E]xit
Enter the Choice: c
Current Balance is 6000

[C]heckBalance
[D]eposit
[W]ithdraw
[T]ransactions
change [P]in
[E]xit
Enter the Choice: t
_______________Transaction History_______________
despoite Amount: 2000
withdraw Amount1000

[C]heckBalance
[D]eposit
[W]ithdraw
[T]ransactions
change [P]in
[E]xit
Enter the Choice: p
Enter New Pin Number: 1235
successfully Pin number changed!

[C]heckBalance
[D]eposit
[W]ithdraw
[T]ransactions
change [P]in
[E]xit
Enter the Choice: e
Thank you for Visit again


'''




























