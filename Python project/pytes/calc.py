
def add(num1:float, num2:float)->float:
    return num1+num2

def sub(num1:float, num2:float)->float:
    return num1-num2

def mul(num1:float, num2:float)->float:
    return num1*num2

def div(num1:float, num2:float)->float:
    if num2 == 0:
        print("Ошибка: На ноль делить нельзя!")
    return num1 / num2

def pro(num1:float, num2:float)->float:
    return num1%num2

def ctep(num1:float, num2:float)->float:
    return num1**num2

