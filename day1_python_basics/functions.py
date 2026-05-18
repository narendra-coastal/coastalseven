def multi(a,b):
    return a*b
def main():
    a=2
    b=5
    print("result=",multi(a,b))
    

main()

def div(c,d):
    return c/d
def main1 ():
    c=10
    d=20
    print("result=",div(c,d))





main1()

#function within function

def f1():
    s = '10'
    def f2():
        print(s)
        
    f2()
f1()