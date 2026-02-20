from numpy import array
t=array([int]*10)
N=int(input("N= "))
for i in range (0,N) :
    t[i]=int(input())
for j in range (N) :
    for i in range(0, N - 1):
        if t[i] > t[i + 1]:
            X = t[i]
            t[i] = t[i + 1]
            t[i + 1] = X
for i in range (0,N) :
    print(t[i])

