from numpy import array
t1=array([int]*N)
t2=array([int]*N)
def saisir() :
    N=int(input("n="))
    return (N)
def remplir(t1,N):
    for i in range(0,N) :
        test=False
        while test==False :
            t1[i]=int(input())
        test= 99<t1[i]<1000
def compte(t1,t2,N) :
    x=0
    for i in range (0,N) :
        x=t1[i]%10*t1[i]
