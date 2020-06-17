#Author : Eugene Parker
#Tasks  : Determining the minimum cost to purchase all product listed (Ecommerce)



#Encapsulating data to make them accessible to only class that extends from this class.
#The use of Polyphorism in Python is also applied in here as well.

#Importing library
import random as r


class Customer:
    def __init__(self,fullname,age,gender,nyrs,status,permission):
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.nyrs = nyrs
        self.status = status
        self.permission = permission

    def getCustomerFullName(self):
        return self.__fullname

    def getAge(self):
        return self.age + "" + "yrs"

    def getUsername(self):
        username = self.fullname[:7]
        return username

    def getGender(self):
        return self.gender

    def getNyrs(self):
        return self.nyrs

    def yearsCheck(self):
        nyrs = self.nyrs
        return nyrs

    def userStatus(self):
        return self.status

    def userPermission(self):
        return self.permission



    
class SystemConfiguration(Customer):
    def __init__(self,fullname,age,gender,nyrs,count,discount,product):
        super().__init__(fullname,age,gender,nyrs)

        self.count = count
        self.discount = discount
        self.product = product
        

    def getDiscount(self,discount):
        return self.discount

    def getProduct(self,product):
        return self.product

   
        




def WiseTech():

    fullname = input("Enter your name: ")
    age = eval(input("Enter your age: "))
    gender = input("Enter your gender: ")
    nyrs = r.randrange(10)
    count = 0

    products = [['10','d0','d1'],['15','EMPTY','EMPTY']]
    discounts = [['10','d0','d1'],['15','EMPTY','EMPTY']]
    status = "inactive"
    permission = 0

    if(fullname != "" and age != "" and gender !=""):
        permission = 0
        status = "active"
        customer = Customer(fullname,age,gender,nyrs,status,permission)
        print(Customer.getAge())
    else:
        return "Please fill in the form"
    
    #system = SystemConfiguration(fullname,age,gender,count,discounts,products)

    #prodarray = system.getProduct(products)
 
    
    #proddiscounts = SystemConfiguration.getProduct(discounts)


WiseTech()






#Users Object
#player1 = Customer("Eugene Parker",22,"male",4,"o","1")
#print(player1.userStatus())

#user1 = System("EP",22,"male",2,5)
#print(user1.nyrs)

    

        

