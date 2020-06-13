
'''
def get_area (pi ,radius):
    area = pi*(radius**2)
    return area , pi


print(get_area(pi =3.14 ,radius=22)) 

'''
def get_area (radius):
    radius+=1
    pi = 3.14
    print(radius)
    print("in_function")
    print("radius = %0.1d" %(radius))
    AA = (pi*(radius*radius))
    print(pi)
    return  AA

# pi =3.14
radius = 20
get_area(50)
print("after function")  
print(radius) 
print(pi)
print(" >>>>>>> ")
print(get_area(radius))


