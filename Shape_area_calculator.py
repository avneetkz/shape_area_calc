# function for calculating areas of different shapes
def calc(shape):
    shape=shape.lower()
    if (shape=='rectangle'):
        l=float(input("Enter length: "))
        b=float(input("Enter breadth: "))
        area= l*b
        print(f'Area of rectangle = {area}')
    
    elif(shape=='square'):
        s=float(input("Enter side of square: "))
        area= s*s
        print(f'Area of square = {area}')
    
    elif(shape=='circle'):
        r=float(input("Enter radius of circle: "))
        pi= 3.14
        area= pi*r*r
        print(f'Area of circle = {area}')
        
    elif(shape=='triangle'):
        h=float(input("Enter heigth of triangle: "))
        b=float(input("Enter base of triangle: "))
        area= 0.5*b*h
        print(f'Area of triangle = {area}')
        
    elif(shape=='parallelogram'):
        h=float(input("Enter heigth of parallelogram: "))
        b=float(input("Enter base of parallelogram: "))
        area= b*h
        print(f'Area of parallelogram = {area}')
        
    else:
        print("Sorry! This shape is not available")
    
# Driver code   
if __name__=="__main__":
    print("\t 1.Square \n")
    print("\t 2.Rectangle \n")
    print("\t 3.Circle \n")
    print("\t 4.Triangle \n")
    print("\t 5.Parallelogram \n")
    
    shape=input("\n Enter your choice: \n")
    calc(shape)
