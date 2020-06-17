import csv

class Registration:
    def __init__(self,fname,lname,birthdate,phone,address,email,password,pin):
        self.fname = fname
        self.lname = lname
        self.birthdate = birthdate
        self.address = address
        self.email = email
        self.password = password
        self.phone = phone
        self.pin = pin
        
    def getFirstname(self):
        return self.fname.lower()
    
    def getLastname(self):
        return self.lname.lower()

    def getBirthdate(self):
        return self.birthdate
    
    def getPhone(self):
        return self.phone
    
    def getUsername(self):
        return self.getFirstname() + "." + self.getLastname()
    
    def getAddress(self):
        return self.address
    
    def getPassword(self):
        return self.password
    
    def getPin(self):
        return self.pin
    
    def getEmail(self):
        return self.email

    def regfunc(self):
        name = self.getFirstname() +"."+ self.getLastname()
        email = self.getEmail()
        password = self.getPassword()
        pin = self.getPin()
        phone =  self.getPhone()
        address =  self.getAddress()
        birthdate = self.getLastname()
        

        file = open('read.txt', 'w')
        file.write(name +"/"+ birthdate +"/"+ phone +"/"+ address +"/"+ email +"/"+ password +"/"+ pin)
        file.close()

        fields = ['Firstname','Lastname','Birthdate','Phone Number','Address','Email', 'Password','Pin']   
      
        # data rows of csv file   
        rows = [ [self.getFirstname(), self.getLastname(),self.getBirthdate(),
                 self.getPhone(),self.getAddress(),self.getEmail(),
                  self.getPassword(),self.getPin()]]   
      
        # name of csv file   
        filename = "read.csv"
      
        # writing to csv file   
        with open(filename, 'w') as csvfile:   

        # creating a csv writer object   
            csvwriter = csv.writer(csvfile)   
          
        # writing the fields   
            csvwriter.writerow(fields)   
          
        # writing the data rows   
            csvwriter.writerows(rows)


user = Registration("Eee","Parker","15/04/1997","000000000","Esa","ema","122","200")
print(user.regfunc())
    
    




    
