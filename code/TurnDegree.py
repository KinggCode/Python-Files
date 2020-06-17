xmin = 0
xmax = 180
ymin = 1.5
ymax = 11

def range_map_degree(angle):
    for i in range(181):
        xrange = xmax-xmin
        yrange = ymax-ymin
        dx_dy = xrange/yrange
        y=((i-xmin) / dx_dy + ymin) 
        #yhat = int(y)
        #print(y)
        dt[i] = y
        #if(i == angle):
         #   return y
        
            


        #for k in range(0,len(cardinal)):
        #    if y in cardinal:
        # #       degree = cardinal[yhat]
        #        state.append(degree)
       # print(degree)
       # sleep(0.5)
       #
    #print(dt)

print(range_map_degree(300))
 
