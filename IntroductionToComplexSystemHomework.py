import random



L = 10
T = 10000
p =  0.8
pc = 0.592746

print("Please select Task Number")
TaskNumber  = int(input())
print(TaskNumber)

def ChangeThem(OriVal, ChangeVal):
    for y in range(0, L):
        for x in range(0, L):
            if A[y][x] == OriVal:
                A[y][x] = ChangeVal



def CheckNear(x, y, A):
    vecmin = []
    if A[y][x] != 0:
        if x == 0 and y== 0:
            if A[y][x] != A[y][x+1]:
                vecmin.append(A[y][x+1])
            elif A[y][x] != A[y+1][x]:
                vecmin.append(A[y+1][x])

        elif x == 0 and y == L-1:
            if A[y][x] != A[y][x+1] and A[y][x+1] != 0:
                vecmin.append(A[y][x+1])
            if A[y][x] != A[y-1][x] and A[y-1][x] != 0:
                vecmin.append(A[y-1][x])

        elif x == L-1 and y == 0:
            if A[y][x] != A[y][x-1] and A[y][x-1] != 0:
                vecmin.append(A[y][x-1])
            if A[y][x] != A[y+1][x] and A[y+1][x] != 0:
                vecmin.append(A[y+1][x])
        elif x == L-1 and y == L-1:
            if A[y][x] != A[y-1][x] and A[y-1][x] != 0:
                vecmin.append(A[y-1][x])
            if A[y][x] != A[y][x-1] and A[y][x-1] != 0:
                vecmin.append(A[y][x-1])

        elif x == L-1 and y != L-1 and y != 0:
            if A[y][x] != A[y][x-1] and A[y][x-1] != 0:
                vecmin.append(A[y][x-1])
            if A[y][x] != A[y+1][x] and A[y+1][x] != 0:
                vecmin.append(A[y+1][x])
            if A[y][x] != A[y-1][x] and A[y-1][x] != 0:
                vecmin.append(A[y-1][x])


        elif y == L-1 and x != L-1 and x != 0:
            if A[y][x] != A[y][x + 1] and A[y][x+1] != 0:
                vecmin.append(A[y][x + 1])
            if A[y][x] != A[y][x - 1] and A[y][x-1] != 0:
                vecmin.append(A[y][x - 1])
            if A[y][x] != A[y - 1][x] and A[y-1][x] != 0:
                vecmin.append(A[y - 1][x])



        elif x == 0 and y != L-1 and y != 0:
            if A[y][x] != A[y][x+1] and A[y][x+1] != 0:
                vecmin.append(A[y][x+1])
            if A[y][x] != A[y+1][x] and A[y+1][x] != 0:
                vecmin.append(A[y+1][x])
            if A[y][x] != A[y-1][x] and A[y-1][x] != 0:
                vecmin.append(A[y-1][x])

        elif y == 0 and x != L-1 and x != 0:
            if A[y][x] != A[y][x+1] and A[y][x+1] != 0:
                vecmin.append(A[y][x+1])
            if A[y][x] != A[y][x-1] and A[y][x-1] != 0:
                vecmin.append(A[y][x-1])
            if A[y][x] != A[y+1][x] and A[y+1][x] != 0:
                vecmin.append(A[y+1][x])


        elif y != 0 and x != 0 and y != L-1 and x != L-1:
            if A[y][x] != A[y][x + 1] and A[y][x+1] != 0:
                vecmin.append(A[y][x + 1])
            if A[y][x] != A[y][x - 1] and A[y][x-1] != 0:
                vecmin.append(A[y][x - 1])
            if A[y][x] != A[y + 1][x] and A[y+1][x] != 0:
                vecmin.append(A[y + 1][x])
            if A[y][x] != A[y-1][x] and A[y-1][x] != 0:
                vecmin.append(A[y-1][x])

    if len(vecmin) == 0:
        return 0
    else:
        return min(vecmin)


if TaskNumber == 6:
    import matplotlib.pyplot as plt
    X1 =[]
    Y1 =[]
    X2 =[]
    Y2 = []
    X3 = []
    Y3 = []
    X4 = []
    Y4 = []
    f1 = open('C:\\Users\DongJae Yoon\Desktop\Python\Dist_p0.592746L10T10000.txt', 'rt', encoding='UTF8')
    f2 = open('C:\\Users\DongJae Yoon\Desktop\Python\Dist_p0.7L10T10000.txt', 'rt', encoding='UTF8')
    f3 = open('C:\\Users\DongJae Yoon\Desktop\Python\Dist_p0.8L10T10000.txt', 'rt', encoding='UTF8')
    f4= open('C:\\Users\DongJae Yoon\Desktop\Python\Dist_p0.5L100T10000.txt', 'rt', encoding='UTF8')

    AxisX = 10000
    AxisY = 0.00000001

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
    plt.plot(X1,Y1, 'ro', label='p = 0.592746' )
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('S')
    plt.ylabel('n_s')
    plt.grid(linestyle=':', color='0.5', linewidth=2)
    plt.legend()
    plt.axis([0, AxisX, AxisY, 1])
    plt.show()



if TaskNumber == 5:
    import matplotlib.pyplot as plt
    X1 =[]
    Y1 =[]
    X2 =[]
    Y2 = []
    X3 = []
    Y3 = []
    f1 = open('C:\\Users\DongJae Yoon\Desktop\Python\AVe_L50T10000.txt', 'rt', encoding='UTF8')
    f2 = open('C:\\Users\DongJae Yoon\Desktop\Python\AVe_L50T10000.txt', 'rt', encoding='UTF8')
    f3 = open('C:\\Users\DongJae Yoon\Desktop\Python\AVe_L100T10000.txt', 'rt', encoding='UTF8')

    while True:
        line1 = f1.readline()
        if not line1:
            break
        K = line1.split()
        X1.append(float(K[0]))
        Y1.append(float(K[2]))

        # if line is empty
        # end of file is reached

    while True:
        line2 = f2.readline()
        if not line2:
            break
        K = line2.split()
        X2.append(float(K[0]))
        Y2.append(float(K[2]))

        # if line is empty
        # end of file is reached

    while True:
        line3 = f3.readline()
        if not line3:
            break
        K = line3.split()
        X3.append(float(K[0]))
        Y3.append(float(K[2]))

        # if line is empty
        # end of file is reached

    f1.close()
    f2.close()
    f3.close()
    plt.plot(X1,Y1, marker = 'o', label='L = 10' )
    plt.plot(X2, Y2, marker = 's', label ='L = 50')
    plt.plot(X3, Y3, marker = '*', label='L = 100')
    plt.xlabel('P')
    plt.ylabel('<S_max>')
    plt.grid(linestyle=':', color='0.5', linewidth=2)
    plt.legend()
    plt.show()




if TaskNumber == 4:
    import matplotlib.pyplot as plt
    X1 =[]
    Y1 =[]
    X2 =[]
    Y2 = []
    X3 = []
    Y3 = []
    f1 = open('C:\\Users\DongJae Yoon\Desktop\Python\AVe_L10T10000.txt', 'rt', encoding='UTF8')
    f2 = open('C:\\Users\DongJae Yoon\Desktop\Python\AVe_L50T10000.txt', 'rt', encoding='UTF8')
    f3 = open('C:\\Users\DongJae Yoon\Desktop\Python\AVe_L100T10000.txt', 'rt', encoding='UTF8')

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

    f1.close()
    f2.close()
    f3.close()
    plt.plot(X1,Y1, 'ro', label='L = 10' )
    plt.plot(X2, Y2, 'bs', label ='L = 50')
    plt.plot(X3, Y3, 'g*', label='L = 100')
    plt.xlabel('P')
    plt.ylabel('P_flow')
    plt.grid(linestyle=':', color='0.5', linewidth=2)
    plt.legend()
    plt.show()

if TaskNumber == 2:
    import time
    start_time = time.time()
    AVGMaxS =[]
    P = []
    VecPFlow = []
    Pv = []

    for p in range(0, 51):
        print(p)
        p = 0.3 + (p * 0.01)
        TotalMaxCounter =[]
        vecP = []
        for t in range(0, T):
            A = [[0] * L for _ in range(L)]
            for y in range(0, L):
                for x in range(0, L):
                    if random.random() < p:
                        A[y][x] = 1
            for x in range(0,L):
                if A[0][x] == 1:
                    A[0][x] = 2
            counter = 2;
            IsBurned = True
            IsReached = False
            while IsBurned == True and IsReached == False:
                IsBurned = False
                for y in range(0, L):
                    for x in range(0, L):
                        if A[x][y] == counter:
                            if x == 0:
                                if y == 0:
                                    if A[x+1][y] == 1:
                                        A[x+1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y+1] == 1:
                                        A[x][y+1] = counter + 1
                                        IsBurned = True
                                elif y == (L-1):
                                    if A[x+1][y] == 1:
                                        A[x+1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y-1] == 1:
                                        A[x][y-1] = counter + 1
                                        IsBurned = True
                                else:
                                    if A[x+1][y] == 1:
                                        A[x+1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y+1] == 1:
                                        A[x][y+1] = counter + 1
                                        IsBurned = True
                                    if A[x][y-1] == 1:
                                        A[x][y-1] = counter + 1
                                        IsBurned = True
                            elif x == (L-1):
                                if y == 0:
                                    if A[x-1][y] == 1:
                                        A[x-1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y+1] == 1:
                                        A[x][y+1] = counter + 1
                                        IsBurned = True
                                elif y == (L-1):
                                    if A[x-1][y] == 1:
                                        A[x-1][y] = counter +1
                                        IsBurned = True
                                    if A[x][y-1] == 1:
                                        A[x][y-1] = counter+1
                                        IsBurned = True
                                else:
                                    if A[x-1][y] == 1:
                                        A[x-1][y] = counter+1
                                        IsBurned = True
                                    if A[x][y + 1] == 1:
                                        A[x][y + 1] = counter + 1
                                        IsBurned = True
                                    if A[x][y - 1] == 1:
                                        A[x][y - 1] = counter + 1
                                        IsBurned = True
                            else:
                                if y == 0:
                                    if A[x-1][y] == 1:
                                        A[x-1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y+1] == 1:
                                        A[x][y+1] = counter + 1
                                        IsBurned = True
                                    if A[x+1][y] == 1:
                                        A[x+1][y] = counter + 1
                                        IsBurned = True
                                elif y == (L-1):
                                    if A[x - 1][y] == 1:
                                        A[x - 1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y - 1] == 1:
                                        A[x][y - 1] = counter + 1
                                        IsBurned = True
                                    if A[x + 1][y] == 1:
                                        A[x + 1][y] = counter + 1
                                        IsBurned = True
                                else:
                                    if A[x-1][y] == 1:
                                        A[x-1][y] = counter+1
                                        IsBurned = True
                                    if A[x][y + 1] == 1:
                                        A[x][y + 1] = counter + 1
                                        IsBurned = True
                                    if A[x][y - 1] == 1:
                                        A[x][y - 1] = counter + 1
                                        IsBurned = True
                                    if A[x+1][y] == 1:
                                        A[x+1][y] = counter + 1
                                        IsBurned = True
                for x in range(0,L):
                    if A[L-1][x] != 0 and A[L-1][x] != 1:
                        IsReached = True
                counter = counter + 1
            if IsReached == True :
                vecP.append(1)
            else:
                vecP.append(0)


            M = 2
            VecK = []
            A = [[0] * L for _ in range(L)]
            vecMaxSum = []
            for y in range(0, L):
                for x in range(0, L):
                    if random.random() < p:
                        A[y][x] = 1
            for x in range(0, L):
                for y in range(0, L):
                    if A[x][y] == 1:
                        if x == 0 and y == 0:
                            A[x][y] = 2
                            M = M + 1
                        elif x == 0:
                            if A[x][y-1] != 0 and A[x][y-1] != 1:
                                A[x][y] = A[x][y-1]
                            else:
                                A[x][y] = M
                                M = M + 1
                        elif y == 0:
                            if A[x-1][y] != 0 and A[x-1][y] != 1:
                                A[x][y] = A[x-1][y]
                            else:
                                A[x][y] = M
                                M = M + 1
                        else:
                            if A[x-1][y] != 0 and A[x-1][y] != 1:
                                A[x][y] = A[x-1][y]
                            elif A[x][y - 1] != 0 and A[x][y - 1] != 1:
                                A[x][y] = A[x][y - 1]
                            else:
                                A[x][y] = M
                                M = M + 1

            for y in range(0,L):
                for x in range(0,L):
                    Checking = CheckNear(x,y,A)
                    if Checking != 0:
                        ChangeThem(A[y][x], Checking)


            VecCount =[]

            for y in range(0,L):
                for x in range(0,L):
                    if(A[y][x] != 0):
                        if len(VecCount) + 1  < A[y][x]:
                            VecCount.append(1)
                        else:
                            VecCount[A[y][x]-2] = VecCount[A[y][x]-2] + 1
            if len(VecCount) == 0:
                TotalMaxCounter.append(0)
                VecCount.append(0)
            else:
                TotalMaxCounter.append(max(VecCount))

        AVGMaxS.append(sum(TotalMaxCounter) / len(TotalMaxCounter))
        P.append(round(p, 4))
        VecPFlow.append(sum(vecP) / len(vecP))

    print(AVGMaxS)
    print(P)
    print(VecPFlow)

    strf1 = "C:\\Users\DongJae Yoon\Desktop\Python"
    strf2 = "\AVe_L" + str(L)
    strf3 = "T"+str(T)
    strf4 = ".txt"
    strf = strf1 + strf2 + strf3 + strf4


    f1 = open(strf,'w',encoding='UTF8')
    for q in range(0, len(AVGMaxS)):
        f1.writelines(str(format(P[q], ".3f")) + "    " + str(format(VecPFlow[q],".3f")) + "    " +  str(format(AVGMaxS[q],".3f")) + "\n")
    f1.close()
    print("--- %s seconds ---" % (time.time() - start_time))

if TaskNumber == 1:
    VecPFlow = []
    Pv = []
    for p in range(0, 20):
        p = p * 0.05
        vecP = []
        for w in range(0, T):

            A = [[0] * L for _ in range(L)]
            for y in range(0, L):
                for x in range(0, L):
                    if random.random() < p:
                        A[y][x] = 1
            for x in range(0,L):
                if A[0][x] == 1:
                    A[0][x] = 2
            counter = 2;
            IsBurned = True
            IsReached = False
            while IsBurned == True and IsReached == False:
                IsBurned = False
                for y in range(0, L):
                    for x in range(0, L):
                        if A[x][y] == counter:
                            if x == 0:
                                if y == 0:
                                    if A[x+1][y] == 1:
                                        A[x+1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y+1] == 1:
                                        A[x][y+1] = counter + 1
                                        IsBurned = True
                                elif y == (L-1):
                                    if A[x+1][y] == 1:
                                        A[x+1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y-1] == 1:
                                        A[x][y-1] = counter + 1
                                        IsBurned = True
                                else:
                                    if A[x+1][y] == 1:
                                        A[x+1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y+1] == 1:
                                        A[x][y+1] = counter + 1
                                        IsBurned = True
                                    if A[x][y-1] == 1:
                                        A[x][y-1] = counter + 1
                                        IsBurned = True
                            elif x == (L-1):
                                if y == 0:
                                    if A[x-1][y] == 1:
                                        A[x-1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y+1] == 1:
                                        A[x][y+1] = counter + 1
                                        IsBurned = True
                                elif y == (L-1):
                                    if A[x-1][y] == 1:
                                        A[x-1][y] = counter +1
                                        IsBurned = True
                                    if A[x][y-1] == 1:
                                        A[x][y-1] = counter+1
                                        IsBurned = True
                                else:
                                    if A[x-1][y] == 1:
                                        A[x-1][y] = counter+1
                                        IsBurned = True
                                    if A[x][y + 1] == 1:
                                        A[x][y + 1] = counter + 1
                                        IsBurned = True
                                    if A[x][y - 1] == 1:
                                        A[x][y - 1] = counter + 1
                                        IsBurned = True
                            else:
                                if y == 0:
                                    if A[x-1][y] == 1:
                                        A[x-1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y+1] == 1:
                                        A[x][y+1] = counter + 1
                                        IsBurned = True
                                    if A[x+1][y] == 1:
                                        A[x+1][y] = counter + 1
                                        IsBurned = True
                                elif y == (L-1):
                                    if A[x - 1][y] == 1:
                                        A[x - 1][y] = counter + 1
                                        IsBurned = True
                                    if A[x][y - 1] == 1:
                                        A[x][y - 1] = counter + 1
                                        IsBurned = True
                                    if A[x + 1][y] == 1:
                                        A[x + 1][y] = counter + 1
                                        IsBurned = True
                                else:
                                    if A[x-1][y] == 1:
                                        A[x-1][y] = counter+1
                                        IsBurned = True
                                    if A[x][y + 1] == 1:
                                        A[x][y + 1] = counter + 1
                                        IsBurned = True
                                    if A[x][y - 1] == 1:
                                        A[x][y - 1] = counter + 1
                                        IsBurned = True
                                    if A[x+1][y] == 1:
                                        A[x+1][y] = counter + 1
                                        IsBurned = True
                for x in range(0,L):
                    if A[L-1][x] != 0 and A[L-1][x] != 1:
                        IsReached = True
                counter = counter + 1
            if IsReached == True :
                vecP.append(1)
            else:
                vecP.append(0)
        VecPFlow.append(sum(vecP)/len(vecP))
        Pv.append(round(p,4))

    print(Pv)
    print(VecPFlow)


if TaskNumber == 3:
    import time
    start_time = time.time()

    TotalCounter = 0
    AVGMaxS =[]
    P = []
    VecPFlow = []
    Pv = []
    VecCount = []
    VecForDist = [0] * ((L * L) + 1)
    p = p
    TotalMaxCounter =[]
    for t in range(0, T):
        M = 2
        VecK = []
        A = [[0] * L for _ in range(L)]
        vecMaxSum = []
        for y in range(0, L):
            for x in range(0, L):
                if random.random() < p:
                    A[y][x] = 1
        for x in range(0, L):
            for y in range(0, L):
                if A[x][y] == 1:
                    if x == 0 and y == 0:
                        A[x][y] = 2
                        M = M + 1
                    elif x == 0:
                        if A[x][y-1] != 0 and A[x][y-1] != 1:
                            A[x][y] = A[x][y-1]
                        else:
                            A[x][y] = M
                            M = M + 1
                    elif y == 0:
                        if A[x-1][y] != 0 and A[x-1][y] != 1:
                            A[x][y] = A[x-1][y]
                        else:
                            A[x][y] = M
                            M = M + 1
                    else:
                        if A[x-1][y] != 0 and A[x-1][y] != 1:
                            A[x][y] = A[x-1][y]
                        elif A[x][y - 1] != 0 and A[x][y - 1] != 1:
                            A[x][y] = A[x][y - 1]
                        else:
                            A[x][y] = M
                            M = M + 1



        for y in range(0,L):
            for x in range(0,L):
                Checking = CheckNear(x,y,A)
                if Checking != 0:
                    ChangeThem(A[y][x], Checking)


        VecCount = []
        for y in range(0,L):
            for x in range(0,L):
                if(A[y][x] != 0):
                    if len(VecCount) + 1  < A[y][x]:
                        VecCount.append(1)
                    else:
                        VecCount[A[y][x]-2] = VecCount[A[y][x]-2] + 1

        VecCount.sort()

        for i in range(0, max(VecCount)+1):
            for l in range(0, len(VecCount)):
                if VecCount[l] == i:
                    VecForDist[i] = VecForDist[i] + 1
                    TotalCounter = TotalCounter + 1



    for s in A:
        print(s)
    print(VecCount)

    for i in range(0, len(VecForDist)):
        VecForDist[i] = VecForDist[i] / TotalCounter

    print(sum(VecForDist))

    strf1 = "C:\\Users\DongJae Yoon\Desktop\Python"
    strf2 = "\Dist_p" + str(p) + "L" + str(L)
    strf3 = "T" + str(T)
    strf4 = ".txt"
    strf = strf1 + strf2 + strf3 + strf4

    s =[]

    for i in range(0, len(VecForDist)):
        s.append(i)



    f1 = open(strf, 'w', encoding='UTF8')
    for q in range(0, len(VecForDist)):
        f1.writelines(str(format(s[q])) + "    " + str(format(VecForDist[q], ".7f")) + "\n")
    f1.close()

    print("--- %s seconds ---" % (time.time() - start_time))

