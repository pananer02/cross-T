from random import randint

def init(tdata,n):
    global RMAX,CMAX,time
    for r in range(55):
        n.append([])
        tdata.append([])
        for c in range(5):                
            n[r].append(0)
            n[r][c] = 0
            tdata[r].append(0)
            tdata[r][c] = 0
    choose()
    RMAX = 0
    CMAX = 0

def enter(a):
    for r in range(55):
        a.append([])
        for c in range(5):
            if(c == 0):
                #Sex
                a[r].append(c)
                a[r][c] = randint(0,1)
            if(c ==1):
                #Pay-type
                a[r].append(c)
                a[r][c] = randint(0,2)
            if(c ==2):
                #Edcation
                a[r].append(c)
                a[r][c] = randint(0,3)
            if(c ==3):
                #Age group
                a[r].append(c)
                a[r][c] = randint(0,2)
            if(c ==4):
                #Days
                a[r].append(c)
                a[r][c] = randint(0,30)       
            

def choose():
    global option1,option2
    print("menu")
    print("0. Exit")
    print("1. Sex")
    print("2. Pay-type")
    print("3. Edcation")
    print("4. Age group")
    option1 = int(input("Input option1 : "))
    while(option1 < 0 or option1 > 4):
        option1 = int(input("Input option1 : "))
    option2 = option1
    while(option1 != 0 and (option1 == option2 or option2 < 0 or option2 >4)):
        option2 = int(input("Input option2 : "))

def calc(a,n):
    global option1,option2,RMAX,CMAX
    for r in range(55):
        o1 = option1-1
        o2 = option2-1
        row = a[r][o1]
        col = a[r][o2]
        tdata[row][col] =  tdata[row][col] + a[r][4]
        n[row][col] = n[row][col] +1
        if(row > RMAX):
            RMAX = row
        if(col > CMAX):
            CMAX = col
    for r in range(RMAX+1):
        for c in range(CMAX+1):
            if(tdata[r][c] > 0):
                tdata[r][c] = tdata[r][c] // n[r][c]
        

def prints():
    global option1,option2,RMAX,CMAX
    print("="*55)
    for r in range(RMAX+1):
        print(r+1,end= ' ')
        print("|",end= ' ')
        for c in range(CMAX+1):
            print(n[r][c],end =' ')
            print("|",end=' ')
        print()
    print("="*55)
    for r in range(RMAX+1):
        print(r+1,end= ' ')
        print("|",end= ' ')
        for c in range(CMAX+1):
            print(tdata[r][c],end =' ')
            print("|",end=' ')
        print()

    
#main
a = []
n = []
tdata = []
option1 = -1
option2 = -1
RMAX = 0
CMAX = 0

init(tdata,n)
enter(a)
while(option1 != 0):
    calc(a,n)
    prints()
    init(tdata,n)

