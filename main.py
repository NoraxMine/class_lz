from octagon import Octagon

def func():
    inp = input('Введите длинну стороны восьмиугольника\n')
    octagon = Octagon(int(inp))
    print(f'Радиус окружности, описсанной около восьмиугольника равен \n{octagon.rad_op()}')
    print(f'Радиус окружности, вписсаной в восьмиугольник равен \n{octagon.rad_vp()}')
    print(f'Радиус окружности, описсанной около восьмиугольника равен \n{octagon.s_op()}')
    print(f'Радиус окружности, вписсаной в восьмиугольник равен \n{octagon.s_vp()}')
    octagon.S()
    octagon.per()
    octagon.paint()
    octagon.S()
    

def main():
    func()

if __name__ == '__main__':
    main()