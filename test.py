def fun(a:str):
    n=len(a)
    res = a[n-2:]+a[0:n-2]
    return res

if __name__ == '__main__':
    s=str(input())
    print(fun(s))