class Door:
    def __init__(self,openDoor,lockedDoor):
        self.openDoor = openDoor
        self.lockedDoor = lockedDoor


    def isLocked(self):
        if(self.isLocked() == True & self.isOpen() == False):
            return "Locked"

    def isOpen(self):
        return self.openDoor

    def unlockDoor(self):
        if(self.isLocked() == True & self.isOpen() == False):
            return "Cannot be opened"
        
    def lockdoor(self):
        if(self.isLocked() == True & self.isOpen() == False):
            self.openDoor = False
            self.lockedDoor = True
    

    def openDoors(self):
        return self.unlockDoor()



    def closeDoor(self):
        if(self.isLocked() == True & self.isOpen() == True):
            return self.openDoor

    

d = Door(False,True)
print(d.isOpen(),d.isLocked())
print(d.openDoors())
print(d.isOpen(),d.isLocked())   
print(d.unlockDoor())
print(d.openDoors())
print(d.isOpen(),d.isLocked())    
        
