X_min = 1.5
X_max = 6
Y_min = 0
Y_max = 90

x = 6
def range_map(x,X_min,X_max,Y_min,Y_max):
    #linear mapping betwwen two range of values
    X_range = X_max-X_min
    Y_range = Y_max-Y_min
    XY_ratio = X_range/Y_range
    y=((x-X_min) / XY_ratio + Y_min) // 1
    return int(y)

print(range_map(x,X_min,X_max,Y_min,Y_max))
