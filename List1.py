import random
import math

print("Please select Task Number")
TaskNumber  = int(input())
print(TaskNumber)

if TaskNumber == 1:
    print("input number?")
    n = input()
    if n.isdigit() != True:
        print("It's not an integer number")
    else:
        if int(n)%2 == 0:
            print("It's an even number")
        else:
            print("It's an odd number")

if TaskNumber == 2:
    a = []
    for i in range(0, 20):
        rn = random.randrange(10,99)
        a.append(rn)
        print(rn)
    AVG = sum(a, 0.0)/len(a)

    print("Mean Value: ")
    print(AVG)
    print("MaxValue: ")
    print(max(a))

if TaskNumber == 3:
    print("Vector dimension?")
    n = int(input())
    v1 =[]
    v2 =[]

    print("input x1 elements")
    for p in range(0,n):
        v1.append(int(input()))
    print("input x2 elements")
    for t in range(0,n):
        v2.append(int(input()))

    upper = 0
    downv1 =0
    downv2 = 0

    for a in range(0,n):
        upper = upper + (v1[a] * v2[a])
        downv1 = downv1 + math.pow(v1[a],2)
        downv2 = downv2 + math.pow(v2[a],2)

    sqrv1 =  math.sqrt(downv1)
    sqrv2 = math.sqrt(downv2)
    product = sqrv1 * sqrv2

    print("the cosine value is:")
    print(upper / product)

if TaskNumber == 4:
    print("input list of elements")
    arr = input().split()
    print("value of C?")
    C = int(input())

    a = int(arr[0])
    b = int(arr[len(arr)-1])

    result = []

    for i in range(0, len(arr)):
        if a < int(arr[i]) and b > int(arr[i]) and int(arr[i])%C == 0:
            result.append(arr[i])

    print("result :")
    print(result)

if TaskNumber == 5:
    print("Input elements of list A")
    A = input().split()
    print("Input elements of list B")
    B = input().split()

    intersec = list(set(A).intersection(B))
    print(intersec)

if TaskNumber == 6:
    print("Input string")
    str = input();
    print(str.replace('b', ""))

if TaskNumber == 7:
    print("Input string")
    str = input();
    letterc =0
    digitc = 0
    for i in range(0, len(str)):
        if str[i].isdigit():
            digitc = digitc +1
        if str[i].isalpha():
            letterc = letterc + 1

    print("number of digits: ")
    print(digitc)
    print("number of letters: ")
    print(letterc)

if TaskNumber == 8:
    print("Input elements")
    l = input().split()
    A =[]
    B =[A]
    for i in range(len(l)):
        old = B[:]
        new = l[i]
        for j in range(len(B)):
            B[j] = B[j] + [new]
        B = old + B
    print(B)

if TaskNumber == 9:
    print("Input string")
    str = input()
    counts = {}
    for i in str:
        counts[i] = counts.get(i, 0) + 1
    print(counts)

    MaxNum = counts.get(max(counts, key=counts.get))
    Ans = []

    for i in counts:
        if counts.get(i) == MaxNum:
            Ans.append(i)


    print("Most frequent is :")
    print(Ans)

if TaskNumber == 10:
    print("Input decimal number")
    str = input()
    ans = "{0:b}".format(int(str))
    print(ans)

if TaskNumber == 11:
    print("Input elements")
    str = input().split()
    Ans = []

    for i in range(0, len(str)):
        if int(str[i]) > 0:
            Ans.append(int(str[i]))
    print(Ans)

if TaskNumber == 12:
    print("Input elements")
    str = input().split()
    Ans = []

    for i in range(0,len(str)):
        if(len(str[i]) < 6):
            Ans.append(str[i])
    print(Ans)


if TaskNumber == 13:
    print("Input elements")
    str = input().split()
    Ans =[]
    MaxT = 0
    for i in range(0, len(str)):
        if MaxT < len(str[i]):
            MaxT = len(str[i])

    for l in range(0, len(str)):
        if MaxT == len(str[l]):
            Ans.append(str[l])

    print(Ans)

if TaskNumber == 14:
    print("Input elements for List A")
    A = input().split()
    print("input elements for List B")
    B = input().split()

    Ans = []
    if(len(A) != len(B)):
        print("number of elements does not match")
    else:
        for i in range(0,len(A)):
            Ans.append(A[i])
            Ans.append(B[i])

    print(Ans)


if TaskNumber == 15:
    print("Input elements")
    a = input().split()

    Digit =[]
    StringL =[]

    for i in range(0, len(a)):

        IsItDigitOnly = True

        for l in range(0, len(a[i])):
            if a[i][l].isdigit() != True:
                IsItDigitOnly = False

        if IsItDigitOnly == True:
            Digit.append(int(a[i]))
        else:
            StringL.append(a[i])

    Digit.sort()
    StringL.sort()

    Ans = StringL + Digit
    print(Ans)