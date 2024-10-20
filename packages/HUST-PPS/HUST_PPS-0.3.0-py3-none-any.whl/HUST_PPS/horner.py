import numpy as np
import math

def Horner(x: np.ndarray,c: float): # a là mảng từ a0 -> an (bậc từ cao -> thấp), c là giá trị của x
    b = [0] * len(x) # Khai báo mảng b có số lượng bằng mảng a
    b[0] = x[0]
    for i in range(1,len(x)):
        b[i] = b[i-1]*c + x[i]
    return np.array(b),b[-1]

def HornerChiaDaThuc(x: np.ndarray, c:float): # a là mảng từ a0 -> an (bậc từ cao -> thấp), c là giá trị trong x - c
    deg = len(x) - 2
    b, _ = Horner(x,c)
    s = ""
    for i in range(0,len(x)-1):
        temp = str(b[i]) + "x**" + str(deg)
        if i != len(x) - 1:
            temp += " + "
        deg -= 1
        s += temp
        
    s += (str(b[-1]) + " / (x - " + str(c) + ")")
    return np.array(b),s

def HornerTinhDaoHam(x: np.ndarray, c:float): # a là mảng từ a0 -> an (bậc từ cao -> thấp), c là giá trị trong x - c
    list_of_b = []
    temp_array = x.copy()
    list_of_b1 = []
    for i in range(0,len(x)):
        sub_a = temp_array[0:len(x)-i]
        b,b1 = Horner(sub_a,c)
        list_of_b.append(b)
        list_of_b1.append(b1)
        temp_array = b.copy()
    for i in range(0,len(list_of_b1)):
        list_of_b1[i] *= math.factorial(i)
    return list_of_b,list_of_b1

def HornerNhanDaThuc(x: np.ndarray, c:float): # a là mảng từ a0 -> an (bậc từ cao -> thấp), c là giá trị trong x - c
    b = [0] * (len(x) + 1)
    b[0] = x[0]
    for i in range(1,len(b)-1):
        b[i] = x[i] - x[i-1]*c
    b[-1] = -x[-1]*c
    return np.array(b)