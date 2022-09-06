from math import *


class Integral:
    def __init__(self):
        self.epselon = pow(10, -6)

    def func(self, x):
        return cos(pow(e,x))

    def right_rectangle(self):
        first_point, last_point = 0, 1
        result = 0
        while first_point + self.epselon < last_point:
            result += self.func(first_point + self.epselon) * self.epselon
            first_point += self.epselon
        return result
        # print("Метод правих прямокутників ")
        # print("Інтеграл == ", result)

    def left_rectangle(self):
        first_point, last_point = 0, 1
        result = 0
        first_point += self.epselon
        while first_point < last_point:
            result += self.func(first_point - self.epselon) * self.epselon
            first_point += self.epselon
        return result
        # print("Метод лівих прямокутників ")
        # print("Інтеграл == ", result)

    def center_rectangle(self):
        first_point, last_point = 0, 1
        result = 0
        while first_point + self.epselon / 2 < last_point:
            result += self.func(first_point + self.epselon / 2) * self.epselon
            first_point += self.epselon
        return result
        # print("Метод центральних прямокутників ")
        # print("Інтеграл == ", result)

    def trapeze(self):
        first_point, last_point = 0, 1
        result = 0
        while first_point + self.epselon < last_point:
            result += ((self.func(first_point) + self.func(first_point + self.epselon)) / 2 * self.epselon)
            first_point += self.epselon
        return result
        # print("Метод трапецій ")
        # print("Інтеграл == ", result)

    def simpson13(self, x0=0, xn=1, n=10):
        # calculating step size
        h = (xn - x0) / n
        # Finding sum
        integration = self.func(x0) + self.func(xn)

        for i in range(1, n):
            k = x0 + i * h

            if i % 2 == 0:
                integration = integration + 2 * self.func(k)
            else:
                integration = integration + 4 * self.func(k)

        # Finding final integration value
        integration = integration * h / 3
        return integration
        # print("Метод сімпсона ")
        # print("Інтеграл == ", integration)


if __name__ == '__main__':
    a = Integral()
    lr = a.left_rectangle()
    rr = a.right_rectangle()
    cr = a.center_rectangle()
    t = a.trapeze()
    s = a.simpson13()
    ser_zn = (lr + rr + cr + t + s) / 5
    print("Метод правих прямокутників ")
    print("Інтеграл == ", rr)
    print("Похибка  == ", ser_zn - rr)
    print("Метод лівих прямокутників ")
    print("Інтеграл == ", lr)
    print("Похибка  == ", ser_zn - lr)
    print("Метод центральних прямокутників ")
    print("Інтеграл == ", cr)
    print("Похибка  == ", ser_zn - cr)
    print("Метод трапецій ")
    print("Інтеграл == ", t)
    print("Похибка  == ", ser_zn - t)
    print("Метод сімпсона ")
    print("Інтеграл == ", s)
    print("Похибка  == ", ser_zn - s)
