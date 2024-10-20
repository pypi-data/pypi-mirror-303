import numpy as np

def FormatNumber(decimals):
    np.set_printoptions(suppress=True, precision=decimals)

def ReadxyFromFile(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            
            if len(lines) < 2:
                raise ValueError("File phải chứa ít nhất hai dòng")
            
            x = np.array([float(num) for num in lines[0].strip().split()])
            y = np.array([float(num) for num in lines[1].strip().split()])
            
            if len(x) != len(y):
                raise ValueError("Số lượng phần tử trong x và y phải giống nhau")
            
            return x, y
    except FileNotFoundError:
        print(f"Không tìm thấy file: {filename}")
    except ValueError as e:
        print(f"Lỗi khi đọc dữ liệu: {e}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
    
    return None, None

def TaoGiaTriXMocCachDeu(x0: np.float64, h:np.float64, n:int):
    list = []
    for i in range(0,n):
        list.append(x0)
        x0 += h
    return np.array(list)