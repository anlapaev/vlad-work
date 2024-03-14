

class Caalculator():
    def __init__(self) -> None:
        
        pass

    def add(self, x1, x2) -> float:
        print("Adding..", x1, x2)
        sum = x1 + x2    #суммируем числа
        l = str(sum)    #преобразуем в строку
        k = len(l)      #считаем колл-во символов
        return round(sum, 10%k)   #округляем
    

    def subtract(self, x1, x2) -> float:
        nesum = x1 - x2
        l = str(nesum)
        k = len(l)
        return round(nesum, 10%k)
    
    def multiply(self, x1, x2) -> float:
        ura = len(str(x1)) + len(str(x2))
        return round(x1 * x2, 10%ura)

    def divide(self, x1, x2) -> float:
        ura = len(str(x1)) + len(str(x2))
        if x2 != 0:
            return round(x1 / x2, 10%ura)
        else:
            return 'zero error'
