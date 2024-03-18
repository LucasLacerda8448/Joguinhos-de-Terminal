import math

def f(x):
    r = 8 - 4.5 * (x - math.sin(x))
    return r

def Bisseccao(a, b, max, e):
    for k in range(max):
        print()
        print("REPETIÇÃO Nº%i" %(k + 1))
        x = (a + b)/2
        if (f(a) * f(x)) < 0:
            b = x
        elif (f(a) * f(x)) > 0:
            a = x
        else:
            print("O intervalo final é [%f, %f]" %(a, b))
            return x
        if abs(b - a) <= e:
            print("O intervalo final é [%f, %f]" %(a, b))
            x = (a + b)/ 2
            return x
        print("O intervalo atual é [%f, %f]" %(a, b))
    print("O intervalo final é [%f, %f]" %(a, b))
    return x

def main():
    print("MÉTODO DA BISSECÇÃO")
    print()
    print("Para iniciar, por favor insira os valores iniciais do intervalo [a,b]:")
    i = 0
    e = 0.001
    while i == 0:
        print("a = ", end="")
        a = int(input())
        print("b = ", end="")
        b = int(input())
        if a > b:
            print("O valor do extremo 'a' deve ser menor que o valor do extremo 'b'.")
            print("Por favor, insira outro intervalo:")
        elif (f(a) * f(b)) > 0:
            print("O intervalo inserido possui os extremos com o mesmo sinal na função.")
            print("Por favor, insira outro intervalo:")
        else:
            print("Intervalo aceito!")
            print()
            i = 1
    if f(a) == 0:
        print("A função é igual a 0 no ponto %i" %a)
    elif f(b) == 0:
        print("A função é igual a 0 no ponto %i" %b)
    else:
        print("Agora, insira o máximo de repetições que o método deve fazer:")
        print("max = ", end="")
        max = int(input())
        bi = Bisseccao(a, b, max, e)
        print("A função é aproximadamente 0 no ponto %f" %bi)

main()
