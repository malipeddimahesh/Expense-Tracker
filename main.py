class expenditure:
    def __init__(self,amount,category,description):
        self.amount=amount
        self.category=category
        self.description=description
    def display(self):
        print("Amount=",self.amount,"\tCategory=",self.category,"\tDescription=",self.description)
def add(expenses):
    a=int(input("Amount: "))
    c=input("Category: ")
    d=input("Description: ")
    s=expenditure(a,c,d)
    expenses.append(s)
    print("expense added sucessfully")
def view(expenses):
    if(len(expenses)==0):
        print("There are no expenses")
        return
    k=1
    for i in expenses:
        print(k,end=".")
        i.display()
        k+=1
def total(e):
    tot=0
    if(len(e)==0):
        print("There are no expenses")
        return
    for i in e:
        tot=tot+i.amount
    print("Total Expenditure: ",tot)
def search(e):
    c=input("Enter the category: ")
    b=False
    k=1
    for i in e:
        if(c==i.category):
            print(k,end=".")
            i.display()
            b=True
        k+=1
    if(b==False):
        print("There is no category found in the expenditure")
def delete_exp(e):
    if len(e) == 0:
        print("No expenses available")
        return
    k=int(input("Enter the serial number of the expense you want to delete: "))
    if(k>len(e) or k<1):
        print("wrong index")
        return
    del(e[k-1])
    print("Expense deleted successfully")
def category_spend(e):
    if len(e) == 0:
        print("No expenses available")
        return
    d={}
    for i in e:
        if(i.category in d):
            d[i.category]+=i.amount
        else:
            d[i.category]=i.amount
    for i in d:
        print(i,d[i])
def highest_cat_spent(e):
    if len(e) == 0:
        print("No expenses available")
        return
    d={}
    for i in e:
        if(i.category in d):
            d[i.category]+=i.amount
        else:
            d[i.category]=i.amount
    maxx=0
    for i in d:
        if(maxx<=d[i]):
            maxx=d[i]
    for i in d:
        if(maxx==d[i]):
            print(i,d[i])
def save(e):
    with open("expenditure.txt","w") as f:
        for i in e:
            f.write(str(i.amount)+","+i.category+","+i.description+"\n")
def load(e):
    try:
        with open("expenditure.txt","r") as f:
            for i in f:
                part=i.strip().split(",")
                s=expenditure(int(part[0]),part[1],part[2])
                e.append(s)
    except FileNotFoundError:
        pass
expenses=[]
load(expenses)
while(True):
    print("1.Add Expense\n2.View Expenses\n3.Total Spending\n4.Search Category\n5.Delete Expense\n6.Category-wise Spending\n7.Highest Spending Category\n8.Exit")

    choice = int(input("Enter a number from the index: "))

    if(choice == 1):
        add(expenses)

    elif(choice == 2):
        view(expenses)

    elif(choice == 3):
        total(expenses)

    elif(choice == 4):
        search(expenses)

    elif(choice == 5):
        delete_exp(expenses)

    elif(choice == 6):
        category_spend(expenses)

    elif(choice == 7):
        highest_cat_spent(expenses)

    elif(choice == 8):
        print("Thank You")
        save(expenses)
        break

    else:
        print("Please enter a number between 1 and 8")
    