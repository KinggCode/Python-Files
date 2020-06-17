class Customer:
    def __init__(self,fname,lname,birthdate,phone,address,profession):
        self.fname = fname
        self.lname = lname
        self.birthdate = birthdate
        self.phone = phone
        self.address = address
        self.profession = profession
        status = False
        account = 0
        balance = 0


    def getFirstname(self):
        return self.fname
    
    def getLastname(self):
        return self.lname
    
    def getBirthdate(self):
        return self.birthdate
    
    def getPhone(self):
        return self.phone
    
    def getAddress(self):
        return self.address

    def getProfession(self):
        return self.profession

    def getDate(self):
        date = self.getBirthdate()
        if(date):
            value = date.split("/")
            day = value[0]
            month = value[1]
            year = value[2]
            return day,month,year
        



customer = Customer('Eugene','Parker','4/04/1997','02020202020','Accra','police')
print(customer.getDate())
