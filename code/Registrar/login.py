from control import *

class Login:
    def __init__(self,email,password,pin):
        self.email = email
        self.password = password
        self.pin = pin
        
    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password

    def getPin(self):
        return self.pin

    def logfun(self):
        email = self.getEmail()
        query = EmailCheck(email)
        return query

user = Login("eee.parker","1234","200")
print(user.logfun())
m 
