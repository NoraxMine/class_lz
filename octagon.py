from math import sqrt, pi, cos, sin
import matplotlib.pyplot as pl


class Octagon:
    
    
    def __init__(self, storona:int):
        self.storona = storona
        self.dig = 45
        self.k = 1 + sqrt(2)
        
    def  rad_op(self) -> float: #Вычисление радиуса описанной окружности
        radius = sqrt((1 + sqrt(2))/((1 + sqrt(2)) - 1)) * self.storona
        return radius
    
    def rad_vp(self) -> float: #Вычисление радиуса вписанной окружности
        radius = (self.storona / 2)* (1 + sqrt(2))
        return radius
    
    def s_op(self):
        S = pi * (self.rad_op ^ 2)
        return S
        
    def s_vp(self):
        S = pi * (self.rad_vp ^ 2)
        return S
    
    def per(self):# Периметр 8-миугольника
        print(f'Периметр 8-миугольника равен: {self.storona * 8}\n')

    def S(self):# Площодь 8-миугольника
        S = 2 * (self.storona ^ 2) * (sqrt(2) + 1)
        print(f'Площадь 8-миугольника равна: {S}\n')
    
    def peaks(self) -> list:# Находим вершины
        peaks_a = []
        peaks_b =[]#Список вершин

        for i in range(8):#Создание списка вершин
            a = self.rad_op() * cos((pi/8) + i * (pi/4))
            b = self.rad_op() * sin((pi/8) + i * (pi/4))
            peaks_a.append(a)
            peaks_b.append(b)

        peaks_a.append(peaks_a[0])#Добавляем первую координату в конец,чтобы замкнуть вершины
        peaks_b.append(peaks_b[0])
        return peaks_a, peaks_b
    
    def paint(self):# Рисуем фигуры
        
        cir1 = pl.Circle((0, 0 ), self.rad_op(), color='black', fill=False)#Описываем  окружность около восьмиугольника
        ax=pl.gca()
        ax.add_patch(cir1)

        cir2 = pl.Circle((0,0 ), self.rad_vp(), color='pink', fill=False)#Вписываем окружность в восьмиугольник
        ax=pl.gca()
        ax.add_patch(cir2)
        
        a,b = self.peaks()#Вершинный восьмиугольник
        pl.plot(a, b, color = 'yellow')

        pl.axis('scaled')#Показываем на экране
        pl.show()

    def __del__(self):
        print('Октагон был удалёт успешно!')
    

def left():

    znach = input('Введите длину стороны 8-миугольника\n')
    oct = Octagon(int(znach))
    print(oct.rad_op())
    print(oct.rad_vp())
    oct.S()
    oct.paint()
    print('-------------')
    a,b = oct.peaks()
    print(a)
    print(b)



def main():
    left()

if __name__ == '__main__':
    main()