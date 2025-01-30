expense ={}

while True:
    print("Menu: ")
    print("1.Add New Expense")
    print("2.View All Expenses")
    print("Calculate Total Amount")
    print("Exit")

    option=int(input('Choose any one'))
    if option==1:
        while True:
            no=input("want to continue (yes/no):")
            if no.lower()=='yes':
                name=input('Enter category name:')
                amount=float(input('Enter category amount:'))
            if no.lower()=='no':
                    break           
    elif option==2:
        print(expense)
    elif option==3:
        print('Total Amount:',sum(expense.value()))
    elif option==4:
        break