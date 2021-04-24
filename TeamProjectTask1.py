import random

print("Please select Task Number")
TaskNumber  = int(input())
print(TaskNumber)
L = 127
p = 0.5
c = 0.15
b = 1 - c
T = 10000



if TaskNumber == 3:
    import matplotlib.pyplot as plt
    X1 =[]
    Y1 =[]
    X2 =[]
    Y2 = []
    X3 = []
    Y3 = []
    X4 = []
    Y4 = []
    f1 = open('C:\\Users\DongJae Yoon\Desktop\Python\L8T100.txt', 'rt', encoding='UTF8')
    f2 = open('C:\\Users\DongJae Yoon\Desktop\Python\L16T100.txt', 'rt', encoding='UTF8')
    f3 = open('C:\\Users\DongJae Yoon\Desktop\Python\L32T100.txt', 'rt', encoding='UTF8')
    f4 = open('C:\\Users\DongJae Yoon\Desktop\Python\L64T100.txt', 'rt', encoding='UTF8')

    AxisX = 0.2
    AxisY = 1

    while True:
        line1 = f1.readline()
        if not line1:
            break
        K = line1.split()
        X1.append(float(K[0]))
        Y1.append(float(K[1]))

        # if line is empty
        # end of file is reached

    while True:
        line2 = f2.readline()
        if not line2:
            break
        K = line2.split()
        X2.append(float(K[0]))
        Y2.append(float(K[1]))

        # if line is empty
        # end of file is reached

    while True:
        line3 = f3.readline()
        if not line3:
            break
        K = line3.split()
        X3.append(float(K[0]))
        Y3.append(float(K[1]))

        # if line is empty
        # end of file is reached

    while True:
        line4 = f4.readline()
        if not line4:
            break
        K = line4.split()
        X4.append(float(K[0]))
        Y4.append(float(K[1]))

        # if line is empty
        # end of file is reached

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    plt.plot(X1,Y1, 'ro-', label='L = 8' )
    plt.plot(X2,Y2, 'bx-', label='L = 16' )
    plt.plot(X3,Y3, 'g*-', label='L = 32' )
    plt.plot(X4,Y4, 'm+-', label='L = 64' )



    plt.grid(linestyle=':', color='0.5', linewidth=2)
    plt.legend()
    plt.show()

















def CheckRight(X, Y, A):
    if X == L-1:
        return False
    elif A[Y][X+1] == -1:
        return True
    else:
        return False
def CheckLeft(X, Y, A):
    if X == 0:
        return False
    elif A[Y][X-1] == -1:
        return True
    else:
        return False
def CheckUp(X, Y, A):
    if Y == 0:
        return False
    elif A[Y-1][X] == -1:
        return True
    else:
        return False
def CheckDown(X, Y, A):
    if Y == L-1:
        return False
    elif A[Y+1][X] == -1:
        return True
    else:
        return False


def CheckNear(X, Y, A):
    summa = 0
    if CheckLeft(X,Y,A):
        summa = summa+1
    if CheckRight(X,Y,A):
        summa = summa +1
    if CheckUp(X, Y, A):
        summa = summa + 1
    if CheckDown(X, Y, A):
        summa = summa + 1
    return summa/4


def Infect(X, Y, A, b):
    Inf_Rate = CheckNear(X,Y,A)
    ran = random.random()
    if Inf_Rate * b > ran:
        A[Y][X] = -1
        return True
    else:
        return False

def Recover(X, Y, A, c):
    ran = random.random()
    if c > random.random():
        A[Y][X] = 0
        return True
    else:
        return False

if TaskNumber == 2:

    Cvec =[]
    AverageSN = []

    for CK in range(0, 50):
        print(CK)
        Cvec.append(c)
        VecRec =[]
        VecSus =[]
        for t in range(0, T):
            A = [[1] * L for _ in range(L)]
            NumberOfInfected = 1
            A[round(L/2)][round(L/2)] = -1
            while NumberOfInfected > 0:
                RandX = random.randint(0,L-1)
                RandY = random.randint(0,L-1)
                if A[RandY][RandX] == 1:
                    if Infect(RandX, RandY, A, b):
                        NumberOfInfected = NumberOfInfected + 1
                elif A[RandY][RandX] == -1:
                    if Recover(RandX, RandY, A, c):
                        NumberOfInfected = NumberOfInfected - 1
            NumRec = 0
            NumSus = 0
            for Y in range(0, L-1):
                for X in range(0, L-1):
                    if A[Y][X] == 0:
                        NumRec =  NumRec + 1
                    elif A[Y][X] == 1:
                        NumSus = NumSus + 1
            VecRec.append(NumRec/(L*L))
            VecSus.append(NumSus/(L*L))
        AverageSN.append(sum(VecRec)/len(VecRec))
        c = c + 0.01

    strf1 = "C:\\Users\DongJae Yoon\Desktop\Python"
    strf2 = "\L" + str(L)
    strf3 = "T" + str(T)
    strf4 = ".txt"
    strf = strf1 + strf2 + strf3 + strf4

    f1 = open(strf, 'w', encoding='UTF8')
    for q in range(0, len(AverageSN)):
        f1.writelines(str(format(Cvec[q], ".3f")) + "    " + str(format(AverageSN[q], ".3f")) + "    " + "\n")
    f1.close()

    print(Cvec)
    print(AverageSN)
