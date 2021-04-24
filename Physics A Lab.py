from random import *
N = 10000
K = 10
Result = []
for l in range(0, K):
    SavingList =[]
    StepBuffer = 0
    for i in range(0, N):
        if(random() >= 0.5):
            StepBuffer = 1
        else:
            StepBuffer = -1
        SavingList.append(StepBuffer)
    Result.append(sum(SavingList))
x_n_square = sum(Result) / len(Result)
VecForSquare = []
for i in range(0, len(Result)):
    VecForSquare.append(Result[i] * Result[i])
x_sqaure_n = sum(VecForSquare) / len(Result)
Sigma = (x_sqaure_n - x_n_square) ** 0.5
print(Sigma)
