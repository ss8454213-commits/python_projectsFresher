#expense tracker project
expensesList= []    #list of expenses in the form of dictionary
print(" WELCOME TO EXPENSE TRACKER: THINK BEFORE YOU BUY ANYTHING")

while True:
    print("======MENU======")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total kharcha ")
    print("Exit")

    choice=int(input(" Please Enter Your Choice: "))

# 1.add expenses
    if(choice==1):
        date=input(" kis date par kharcha kiya tha ?:")
        category=input("kis type ka kharcha kiya tha? (food,travel,makeup,books,accessories):")
        description=input("more details about the category of goods :")
        amount=float(input("enter the amount :"))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expensesList.append(expense)
        print("\n DONE DUDE. expenses is added successfully")
        

# 2.view all expenses
    elif(choice==2):
        if(len(expensesList)==0):
            print("No Expenses Added. jao phle khrcha karo")
        else:
            print("==== This is All Your Expense====")
            count=1
            for eachkharcha in expensesList:
                print(f"kharcha Number {count}-->  {eachkharcha["date"]},{eachkharcha["category"]},{eachkharcha["description"]},{eachkharcha["amount"]}")
                count+=1

#3.  view all spending 
    elif(choice==3):
        total=0
        for eachkharcha in expensesList:
            total=total + eachkharcha["amount"]
            print("\n TOTAL KHARCHA =",total)

#4. exit     
    elif(choice==4):
        print("DHANYAWAAD! apne hmara system use kiya")
        break

    else:
        print("INVALID CHOICE. try again")
    
    
      


                
            
        

