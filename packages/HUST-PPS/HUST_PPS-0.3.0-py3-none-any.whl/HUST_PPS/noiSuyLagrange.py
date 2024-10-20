import numpy as np
from HUST_PPS import HornerNhanDaThuc, HornerChiaDaThuc

def LapBangTichLagrange(x: np.ndarray):
    list_of_arrays = []
    b = [1]
    max_length = len(x) + 1
    temp = np.zeros(max_length)
    temp[-1] = 1
    list_of_arrays.append(temp)
    for i in range(0,len(x)):
        b1 = HornerNhanDaThuc(b,x[i])
        b2 = np.zeros(max_length)
        b2[-len(b1):] = b1
        list_of_arrays.append(b2)
        b = b1.copy()
    return np.array(list_of_arrays)

def LapBangThuongLagrange(x: np.ndarray):
    list_of_c = []
    lap_bang_tich = LapBangTichLagrange(x)[-1]
    for i in range(0,len(x)):
        c, _ = HornerChiaDaThuc(lap_bang_tich,x[i])
        list_of_c.append(c)
    return np.array(list_of_c)
    
def LapBangTinhCyLagrange(x: np.ndarray, y: np.ndarray):
    ones_matrix = np.ones((len(x),len(x)))
    for i in range(0,len(x)):
        for j in range(0,len(x)):
            if i != j:
                ones_matrix[i,j] = x[j] - x[i]
    return ones_matrix    
    
def TinhCyLagrange(x: np.ndarray, y: np.ndarray):
    c = [0] * len(x)
    for i in range(0,len(y)):
        res = 1
        for j in range(0,len(x)):
            if i != j:
                res *= (x[i] - x[j])
        c[i] = y[i] / res
    return np.array(c)

def DaThucNoiSuyLagrange(x: np.ndarray, y: np.ndarray):
    A = LapBangThuongLagrange(x)[:, :-1]
    Cy = TinhCyLagrange(x,y)
    return Cy @ A

def TinhDyLagrangeMocCachDeu(y: np.ndarray, n: int):
    res = np.zeros((n+1))
    for i in range(0,n+1):
        temp = 1
        for j in range(0,n+1):
            if j != i:
                temp *= (i - j)
        res[i] = y[i] / temp
    return res

def LapBangTichLagrangeMocCachDeu(n: int):
    res = np.zeros((n+1))
    for i in range(1,n+1):
        res[i] = i
    return LapBangTichLagrange(res)

def LapBangThuongLagrangeMocCachDeu(n: int):
    list_of_c = []
    res = np.zeros((n+1))
    for i in range(1,n+1):
        res[i] = i
    
    lap_bang_tich = LapBangTichLagrangeMocCachDeu(n)[-1]
    for i in range(0,n+1):
        c, _ = HornerChiaDaThuc(lap_bang_tich,res[i])
        list_of_c.append(c)
    return np.array(list_of_c)

def DaThucNoiSuyLagrangeMocCachDeuThamSoT(y: np.ndarray,n: int):
    Dy = TinhDyLagrangeMocCachDeu(y,n)
    A = LapBangThuongLagrangeMocCachDeu(n)[:,:-1]
    
    return Dy @ A