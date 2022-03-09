#how to make a triangle with for in python

#first you need to use the for loop

for i in range(5,0,-1):
    #then you need another for loop
    for j in range(0,i):
            print('*', end="")
    print("")

#if you want to make a not upside down triangle

for i in range(0,6):
    for j in range(0,i):
        print('*', end="")
    print("")