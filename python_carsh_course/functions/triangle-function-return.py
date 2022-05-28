
h= int(input("Enter Height:"))
b= int(input("Enter base:"))

def triangle_area(height,base):
    area=(height*base)/2
    return area

tri_area = triangle_area(h,b)

print("Triangle area is:", tri_area)