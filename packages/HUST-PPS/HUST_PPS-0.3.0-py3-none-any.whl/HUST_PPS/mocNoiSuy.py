import numpy as np

def TinhMocNoiSuy(a: float,b: float,n: int):
    print("Các mốc nội suy tối ưu là nghiệm của đa thức Chebysev bậc", n-1)
    list_x = []
    for i in range(0,n):
        t = np.cos(((2*i+1)/(2*(n)))*np.pi)
        x = 0.5*(b-a)*t + 0.5*(a+b)
        list_x.append(x)
    list_x.sort()
    return np.array(list_x)