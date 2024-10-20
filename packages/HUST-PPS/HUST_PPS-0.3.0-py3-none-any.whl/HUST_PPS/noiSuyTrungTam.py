import numpy as np
from HUST_PPS import TinhBangSaiPhan, LapBangTichLagrange
import math

def TinhBangSaiPhanGaussI(x: np.ndarray, y:np.ndarray, n: int): # n là số có dạng 2k+1
    bang_sai_phan = TinhBangSaiPhan(x,y)
    index = int(n / 2)
    list = []
    list.append(bang_sai_phan[index,1])
    j = 2
    cnt = 2
    while j < bang_sai_phan.shape[1] and index < n:
        if cnt == 2:
            index += 1
            cnt = 0
        list.append(bang_sai_phan[index,j])
        j += 1
        cnt += 1
    return np.array(list)

def TinhCySaiPhanGaussI(x: np.ndarray, y:np.ndarray, n: int):
    he_so = TinhBangSaiPhanGaussI(x,y,n)
    for i in range(0,len(he_so)):
        he_so[i] /= math.factorial(i)
    return he_so

def LapBangTichGaussI(n: int): # n dạng 2k+1
    k = int(n/2)
    cnt = 0
    list = []
    while (True):
        if cnt == 0:
            list.append(0)
        elif cnt == k:
            list.append(k)
            break
        else:
            list.append(cnt)
            list.append(-1*cnt)
        cnt += 1
    return LapBangTichLagrange(list)

def DaThucNoiSuyTrungTamGaussI(x: np.ndarray, y:np.ndarray, n: int):
    B = LapBangTichGaussI(n)
    A = TinhCySaiPhanGaussI(x,y,n)
    
    return A @ B

def TinhBangSaiPhanGaussII(x: np.ndarray, y:np.ndarray, n: int): # n là số có dạng 2k+1
    bang_sai_phan = TinhBangSaiPhan(x,y)
    index = int(n / 2)
    list = []
    list.append(bang_sai_phan[index,1])
    j = 2
    cnt = 1
    while j < bang_sai_phan.shape[1] and index < n:
        if cnt == 2:
            index += 1
            cnt = 0
        list.append(bang_sai_phan[index,j])
        j += 1
        cnt += 1
    return np.array(list)

def TinhCySaiPhanGaussII(x: np.ndarray, y:np.ndarray, n: int):
    he_so = TinhBangSaiPhanGaussII(x,y,n)
    for i in range(0,len(he_so)):
        he_so[i] /= math.factorial(i)
    return he_so

def LapBangTichGaussII(n: int): # n dạng 2k+1
    k = int(n/2)
    cnt = 0
    list = []
    while (True):
        if cnt == 0:
            list.append(0)
        elif cnt == k:
            list.append(-1*k)
            break
        else:
            list.append(-1*cnt)
            list.append(cnt)
        cnt += 1
    return LapBangTichLagrange(list)

def DaThucNoiSuyTrungTamGaussII(x: np.ndarray, y:np.ndarray, n: int):
    B = LapBangTichGaussII(n)
    A = TinhCySaiPhanGaussII(x,y,n)
    
    return A @ B

def LapBangTichSterling(n: int):
    list = []
    for i in range(1, int(math.sqrt(n)) + 1):
        list.append(i*i)
    return LapBangTichLagrange(list)

def TinhCyChanSterling(x: np.ndarray, y:np.ndarray, n:int):
    he_so = TinhCySaiPhanGaussI(x,y,n)
    list = []
    for i in range(0,n):
        if i % 2 == 0:
            list.append(he_so[i])
    return np.array(list)

def TinhBangSaiPhanLeSterling(x: np.ndarray, y:np.ndarray, n:int):
    k = int(n/2)
    bang_sai_phan = TinhBangSaiPhan(x,y)
    list = []
    for j in range(2,bang_sai_phan.shape[1],2):
        sum = (bang_sai_phan[k,j] + bang_sai_phan[k+1,j]) / 2
        list.append(sum)
        k += 1
        if k >= n:
            break
    return np.array(list)

def TinhCyLeSterling(x: np.ndarray, y:np.ndarray, n:int):
    A = TinhBangSaiPhanLeSterling(x,y,n)
    j = 1
    for i in range(0,len(A)):
        A[i] /= math.factorial(j)
        j += 2
    return A

def DaThucNoiSuyTrungTamSterling(x: np.ndarray, y:np.ndarray, n:int):
    Cy_chan = TinhCyChanSterling(x,y,n)
    Cy_le = TinhCyLeSterling(x,y,n)
    A = LapBangTichSterling(n)
    Cy_chan = Cy_chan[1:]
    ar1 = Cy_chan @ A
    ar2 = Cy_le @ A
    k = int(n/2)
    ar1 = np.append(ar1,y[k])
    length = len(ar1) + len(ar2)
    ans = np.zeros(length)
    index = 0
    for i in range(0,length,2):
        ans[i] = ar1[index]
        index += 1
    index = 0
    for i in range(1,length,2):
        ans[i] = ar2[index]
        index += 1
    return ans