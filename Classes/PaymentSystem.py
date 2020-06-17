#Author : Eugene Parker
#Tasks : Empployees Payment system

#Creating a Parent Class ----> Person
class Person:
    def __init__(self,firstName,lastName,age,gender,residence,mobileNo):
        self.__firstName = firstName
        self.__lastName = lastName
        self.fullname = firstName.title() + lastName.title()
        self.__age = age
        self.__gender = gender
        self.__residence = residence
        self.__mobileNo = mobileNo
        self.__email = firstName.lower() + "." + lastName.lower() + "@company.com"

#Creating methods to encapsulate data and restrict direct access to values
    def getFirstName(self):
        return self.__firstName

    def getlastName(self):
        return self.__lastName

    def getFullName(self):
        return '{} {}'.format(self.__firstName,self.__lastName)

    def getAge(self):
        return self.__age

    def getGender(self):
        return self.__gender

    def getEmail(self):
        return self.__email

#Creating a Child Class from Parent Class ----> Employee
class Employees(Person):
    def __init__(self,firstName,lastName,age,gender,residence,mobileNo,position,pay):
        super().__init__(firstName,lastName,age,gender,residence,mobileNo)
        
        self.position = position
        self.pay = pay

    def getResidence(self):
        return self.residence
    
    def getMobileNo(self):
        return self.mobileNo

    def getposition(self):
        return self.position

    def getPay(self):
        return self.pay


class Managers(Person):
    def __init__(self,firstName,lastName,age,gender,residence,mobileNo,pay,employee ="none"):
        super().__init__(firstName,lastName,age,genderresidence,mobileNo)


    
#Creating Instance of the Employee Class
employee1 = Employees("Eugene","Parker",22,"male","Accra","0207973714","programmer",2000)


#Print Statements
#print(employee1.getAge())
#print(employee1.getEmail())


#Creating the Formula ----> Salary Class


#Creating a Company System
class Company:
    def __init__(self,companyName,industry,revenue,expenditure):
        self.__companyName = compnayName
        self.__industry = industry
        self.__revenue = revenue
        self.__expenditure = expenditure

    def getCompanyName():
        return self.__companyName

    def getIndustry(self):
        return self.__industry

    def getRevenue(self):
        return self.__revenue

    def getExpenditure(self):
        return self.__expenditure


class RevenueGenerate:
    def __init__(self,transaction_no,description,amount):
        self.__transaction_no = transaction_no
        self.__description = description
        self.__amount = amount

    def getTransNo(self):
        return self.__transaction_no

    def getTransDesc(self):
        return self.__description

    def getTransAmount(self):
        return self.__amount


amountlist = []
transactions = []
clients =[]
total = 0

user_input = eval(input("Please type the no of transactions you have to input: "))

for i in range(user_input):
    trans_no = input("Enter transaction Number: ")
    trans_desc = input("Enter Description: ")
    trans_amt= eval(input("Enter Amount: "))
    amountlist.append(trans_amt)
    transactions.append(trans_desc)
    clients.append(trans_desc)

    for total in amountlist:
        total += total

print()
print()
print("Your Total revenue is {}".format(total))
print("Transations No {}".format(transactions))
print("Clients involved {}".format(clients))
print("Amount list {}".format(amountlist))

#Creating Instance of the RevenueGenerate Class
trans1 = RevenueGenerate(trans_no,trans_desc,trans_amt)




        
        

        

