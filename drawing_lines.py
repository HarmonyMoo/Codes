import matplotlib.pyplot as plt

print("Enter the value of x1: ")
x1 = int(input())
print("Enter the value of x2: ")
x2 = int(input())
print("Enter the value of y1: ")
y1 = int(input())
print("Enter the value of y2: ")
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

if abs(dx) > abs(dy):
    steps = abs(dx)
else:
    steps = abs(dy)

xincrement = dx/steps
yincrement = dy/steps

i = 0;

xcoordinates = [];
ycoordinates = [];


while i < steps:
    i +=1
    x1 = x1 + xincrement
    y1 = y1 + yincrement
    print("X: ",x1, "Y: ", y1)
    xcoordinates.append(x1)
    ycoordinates.append(y1)

plt.plot(xcoordinates, ycoordinates)

#Naming the Axis
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

#Graph title
plt.title("DDA Algorithm")

#show the plot

plt.show()

import matplotlib.pyplot as plt

plt.title("Midpoint Line Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def midpoint(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Initialize the decision parameter
    d  = dy - (dx/2)
    x = x1
    y = y1

    print(f"x = {x}, y = {y}")
    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    while (x<x2):
        x = x + 1
        # East is Chosen
        if (d<0):
            d = d + dy

        # North East is Chosen
        else:
            d = d + (dy - dx)
            y = y + 1

        xcoordinates.append(x)
        ycoordinates.append(y)
        print(f"x = {x}, y = {y}")
    plt.plot(xcoordinates, ycoordinates)
    plt.show()

if __name__=="__main__":
    x1 = int(input("Enter the starting point of x: "))
    y1 = int(input("Enter the starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))

    midpoint(x1, y1, x2, y2)

import matplotlib.pyplot as plt
plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def bres(x1,y1,x2,y2):
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2*dy - dx
    print(f"x = {x}, y = {y}")
    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        print(f"x = {x}, y = {y}")
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates)
    plt.show()


def main():
    x1 = int(input("Enter the Starting point of x: "))
    y1 = int(input("Enter the Starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))

    bres(x1, y1, x2, y2)

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt

plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def function(x1,y1,x2,y2):
    x,y = x1,y1
    w = abs(x2 - x1)
    h = abs(y2 -y1)
    gradient = h/float(w)

    if gradient > 1:
        h, w = w, h
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    F = 2*h-w
    print(f"x = {x}, y = {y}")
    xcoordinates = [x]
    ycoordinates = [y]

    for k in range(2, dx + 2):
        if F < 0:
            F += 2*h
        else:
            F += 2*(h-w)
            y = y+1

        x = x + 1 if x < x2 else x - 1

        print(f"x = {x}, y = {y}")
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates)
    plt.show()


def main():
    x1 = int(input("Enter the Starting point of x: "))
    y1 = int(input("Enter the Starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))

    bres(x1, y1, x2, y2)

if __name__ == "__main__":
    main()
