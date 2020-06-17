# Complete the maximumToys function below.
def maxtoys(price,leng):
    if(price != leng):
        return True
        

def maximumToys(price,amt):
    ava_price = []
    accum = 0
    
    itemlist = {
    "item1" : {
    "item_name" : "batman",
    "item_price" : 1
                },
    "item2" : {
    "item_name" : "superman",
    "item_price" : 2
                },
    "item3" : {
    "item_name" : "motor car",
    "item_price" : 3
                },
    "item4" : {
    "item_name" : "ludo",
    "item_price" : 4
                }
    }
    #for i in range(len(itemlist)):
    for k in itemlist:
        prices = int(itemlist[k]["item_price"])
        ava_price.append(prices)
        #print(ava_price)

    for pric in ava_price:
        if(pric < amt):
            #print(pric)
            accum = accum + pric
        print(accum)
        mt = maxtoys(accum,amt)
        if(mt):
            print("false")

        else:
            print("rue")
            
            
           
            
            
                

    

    

maximumToys(9,10)
