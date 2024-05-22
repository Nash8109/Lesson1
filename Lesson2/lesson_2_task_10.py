proc = 0.1
def bank(x,y):
    for i in range(1,int(y)+1):
        z=x*proc
        x=x+z
        print (x)

bank(int(input("Введите сумму вклада: ")), int(input ("Введите срок вклада: ")))