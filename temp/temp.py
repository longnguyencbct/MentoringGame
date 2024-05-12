def f1(x):
    ans=0
    for i in range(x):
        ans+=i
    return ans
def f2(x):
    ans=0
    for i in range(x):
        ans+=i**2
    return ans
#####################################################
#           COMBINATION OF f1(x) AND f2(x)          #
#####################################################
def f3(x):
    ans=[0,0]
    for i in range(x):
        ans[0]+=i
        ans[1]+=i**2
    return ans
#OR
def f4(x):#python only
    ans1,ans2=0,0 
    for i in range(x):
        ans1+=i
        ans2+=i**2
    return ans1,ans2
arr=[]
arr.so
