def calArea(a,b):
    area      = a*b
    perimeter = 2*(a+b)
    print('area=',area)
    return area,perimeter

# main program
a1,p1           = calArea(2,3)
a2,p2           = calArea(1,3)
total_area      = a1 + a2
total_perimeter = p1 + p2 

print('total_area',total_area)
print('total_perimeter',total_perimeter)
