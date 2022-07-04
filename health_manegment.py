#health mangement system
# clients :- Sachin ,  Skashee , Nitesh
# def detdate():
#     import datetime
#     return datetime.datetime.now()


#Total files 6
# write a function that when executed task as input client name
#One more function to retrieve exercise of food fir any client


import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if k ==1 :
        c = int(input("Enter 1 for exercise and 2 for food ! "))
        if(c==1):
            value = input("type here \n")
            with open("sachin_ex.txt" , "a")as op:
                op.write(str([str(gettime())])+":"+value+"\n")
                print("succefully written")
        elif c==2:
            value = input("type hare \n")
            with open("sachin_food.txt" , "a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
                print("succefully written")

    elif k==2:
        c = int(input("Enter 1 for exercise and 2 for food ! "))
        if(c==1):
            value = input("type here \n")
            with open("sakshii_ex.txt" , "a")as op:
                op.write(str([str(gettime())])+":"+value+"\n")
                print("succefully written")
        elif c==2:
            value = input("type hare \n")
            with open("sakshii_food.txt" , "a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
                print("succefully written")

    elif k==3:
        c = int(input("Enter 1 for exercise and 2 for food ! "))
        if (c == 1):
            value = input("type here \n")
            with open("nitesh_ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
                print("succefully written")
        elif c == 2:
            value = input("type hare \n")
            with open("nitesh_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
                print("succefully written")

        else:
            print("plz Enter valid input 1 (sachin) , 2 (sakshii) , 3 (nitesh) \n")

def retrieve(k):
    if k==1:
        c = int(input("Enter 1 for exercise and 2 for food ! "))
        if(c==1):
            with open("sachin_ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif (c==2):
            with open("sachin_food.txt") as op:
                for i in op:
                    print(i,end="")

    elif k ==2:
        c = int(input("Enter 1 for exercise and 2 for food ! "))
        if (c == 1):
            with open("sakshii_ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("sakshii_food.txt") as op:
                for i in op:
                    print(i, end="")

    elif k==3:
        c = int(input("Enter 1 for exercise and 2 for food ! "))
        if (c == 1):
            with open("nitesh_ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("nitesh_food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (sachin, skashii , nitesh ) ")

print("health management system ")
a = int(input("press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("press 1 for sachin , 2 for sakshii and 3 for nitesh "))
    take(b)

else:
    b = int(input("press 1 for sachin , 2 for sakshii and 3 for nitesh "))
    retrieve(b)