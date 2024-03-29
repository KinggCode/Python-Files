xmin = 0
xmax = 180
ymin = 1.5
ymax = 11
from time import time,sleep


def range_map_degree(angle):
    dt = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 1.0, 6: 1.0, 7: 1.0, 8: 1.0,
      9: 1.0, 10: 2.0, 11: 2.0, 12: 2.0, 13: 2.0, 14: 2.0, 15: 2.0, 16: 2.0, 17: 2.0,
      18: 2.0, 19: 2.0, 20: 2.0, 21: 2.0, 22: 2.0, 23: 2.0, 24: 2.0, 25: 2.0, 26: 2.0,
      27: 2.0, 28: 2.0, 29: 3.0, 30: 3.0, 31: 3.0, 32: 3.0, 33: 3.0, 34: 3.0, 35: 3.0, 36: 3.0,
      37: 3.0, 38: 3.0, 39: 3.0, 40: 3.0, 41: 3.0, 42: 3.0, 43: 3.0, 44: 3.0, 45: 3.0, 46: 3.0, 47: 3.0,
      48: 4.0, 49: 4.0, 50: 4.0, 51: 4.0, 52: 4.0, 53: 4.0, 54: 4.0, 55: 4.0, 56: 4.0, 57: 4.0, 58: 4.0, 59: 4.0,
      60: 4.0, 61: 4.0, 62: 4.0, 63: 4.0, 64: 4.0, 65: 4.0, 66: 4.0, 67: 5.0, 68: 5.0, 69: 5.0, 70: 5.0, 71: 5.0, 72: 5.0,
      73: 5.0, 74: 5.0, 75: 5.0, 76: 5.0, 77: 5.0, 78: 5.0, 79: 5.0, 80: 5.0, 81: 5.0, 82: 5.0, 83: 5.0, 84: 5.0, 85: 5.0,
      86: 6.0, 87: 6.0, 88: 6.0, 89: 6.0, 90: 6.0, 91: 6.0, 92: 6.0, 93: 6.0, 94: 6.0, 95: 6.0, 96: 6.0, 97: 6.0, 98: 6.0,
      99: 6.0, 100: 6.0, 101: 6.0, 102: 6.0, 103: 6.0, 104: 6.0, 105: 7.0, 106: 7.0, 107: 7.0, 108: 7.0, 109: 7.0, 110: 7.0,
      111: 7.0, 112: 7.0, 113: 7.0, 114: 7.0, 115: 7.0, 116: 7.0, 117: 7.0, 118: 7.0, 119: 7.0, 120: 7.0, 121: 7.0, 122: 7.0,
      123: 7.0, 124: 8.0, 125: 8.0, 126: 8.0, 127: 8.0, 128: 8.0, 129: 8.0, 130: 8.0, 131: 8.0, 132: 8.0, 133: 8.0, 134: 8.0,
      135: 8.0, 136: 8.0, 137: 8.0, 138: 8.0, 139: 8.0, 140: 8.0, 141: 8.0, 142: 8.0, 143: 9.0, 144: 9.0, 145: 9.0, 146: 9.0,
      147: 9.0, 148: 9.0, 149: 9.0, 150: 9.0, 151: 9.0, 152: 9.0, 153: 9.0, 154: 9.0, 155: 9.0, 156: 9.0, 157: 9.0, 158: 9.0,
      159: 9.0, 160: 9.0, 161: 9.0, 162: 10.0, 163: 10.0, 164: 10.0, 165: 10.0, 166: 10.0, 167: 10.0, 168: 10.0, 169: 10.0,
      170: 10.0, 171: 10.0, 172: 10.0, 173: 10.0, 174: 10.0, 175: 10.0, 176: 10.0, 177: 10.0, 178: 10.0, 179: 10.0, 180: 11.0}
    
    return dt[angle]


    #cardinal = {0:"0°",1:"15°",2:"30°",3:"45°",5:"60°",6:"90°",7:"115°",8:"130°",9:"145°",10:"165°",11:"180°"}
    #state = []
    #dt = {}
    #for i in range(181):
        #xrange = xmax-xmin
        #yrange = ymax-ymin
        #dx_dy = xrange/yrange
        #y=((i-xmin) / dx_dy + ymin) // 1
        #yhat = int(y)
        #print(y)
        #dt[i] = y
        #for k in range(0,len(cardinal)):
        #    if y in cardinal:
        # #       degree = cardinal[yhat]
        #        state.append(degree)
       # print(degree)
       # sleep(0.5)
       #
    #print(dt)

#print(range_map_degree(xmin,xmax,ymin,ymax))
print(range_map_degree(90))
    
 
