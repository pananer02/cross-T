from random import randint

def init(tdata,ct):
    for r in range(0,150):
        tdata.append([])
        ct.append([])
        for c in range(0,5):   
            tdata[r].append(0)
            ct[r].append(0)

def enter(tdata):
    for r in range(150):
        tdata.append([])
        for c in range(5):
            tdata[r][c] = randint(10,60)
            #Ages
            if(c == 0):
                if(tdata[r][0] < 21):
                    tdata[r][0] = 0
                else:
                    if(tdata[r][0] < 40):
                        tdata[r][0] = 1
                    else:
                        tdata[r][0] = 2
            if(c ==1):
                #education
                tdata[r].append(c)
                tdata[r][c] = randint(0,2)
            if(c ==2):
                #Yes or No
                tdata[r].append(c)
                tdata[r][c] = randint(0,1)
            if(c ==3):
                #Yes or No
                tdata[r].append(c)
                tdata[r][c] = randint(0,1)
            if(c ==4):
                #Yes or No
                tdata[r].append(c)
                tdata[r][c] = randint(0,1)     

def choose():
    global option1,option2
    print("menu")
    print('1.Ages')
    print('2.Education')
    print('3.Yes or No')
    print('4.Yes or No')
    print('5.Yes or No')
    option1 = int(input("Input option1 : "))
    while(option1 < -1 or option1 > 5):
        option1 = int(input("Input option1 : "))
    option2 = option1
    while(option1 != 0 and (option1 == option2 or option2 < 0 or option2 >5)):
        option2 = int(input("Input option2 : "))

def calc():
    global option1,option2,RMAX,CMAX
    RMAX = 0
    CMAX = 0
    for a in range(150):
        r = tdata[a][option1-1]
        c = tdata[a][option2-1]
        ct[r][c] += 1
        if(r > RMAX):
            RMAX = r
        if(c > CMAX):
            CMAX = c

def prints():
    global option1,option2,RMAX,CMAX
    print("="*55)
    for r in range(RMAX+1):
        print(r+1,end= ' ')
        print("|",end= ' ')
        for c in range(CMAX+1):
            print(ct[r][c],end =' ')
            print("|",end=' ')
        print()
    
#main
ct = []
tdata = []
option1 = -1
option2 = -1
RMAX = 0
CMAX = 0

init(tdata,ct)
enter(tdata)
choose()
while(option1 != -1):
    calc()
    prints()
    init(tdata,ct)
    choose()

