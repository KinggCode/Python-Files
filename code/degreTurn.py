global activateFlag,deactivateFlag,counter,xmin,xmax,ymin,ymax
activateFlag = 'Active'
deactiveFlag = 'Disable'
xmin = 0
xmax = 180
ymin = 1.5
ymax = 11


from time import sleep

class Swing():
    def __init__(self,swingId,swingPin,swingName,swingStatus,srtTime,endTime,resetTime):
        self.swingId = swingId
        self.swingPin = swingPin
        self.swingName = swingName
        self.swingStatus = swingStatus
        self.srtTime = srtTime
        self.endTime = endTime
        self.resetTime = resetTime
    

        


    def terminate(self):
            self.running = False

    def SetTurn(self,angle):
        if(self.swingStatus == deactiveFlag):
            return self.swingStatus

        elif(self.swingStatus == activateFlag):
            global xmin,ymin,xmax

            for i in range(181):
                xrange = xmax-xmin
                yrange = ymax-ymin
                dx_dy = xrange/yrange
                y=((i-xmin) / dx_dy + ymin)
                #yhat = int(y)
                #print(y)
                dt[i] = y
                #if(i == angle):
                 #   print(y)
            
           
            
            

swinA = Swing("01",22,"Swing A","Active",2,3,0.5)
swinA.SetTurn(180)
