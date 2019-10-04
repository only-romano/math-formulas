from decimal import Decimal

# Вычисляет любое значение числа фиббоначи по порядковому номеру
GOLDEN_D = Decimal((1 + 5 ** 0.5) / 2)
GOLDEN = (1 + 5 ** 0.5) / 2

def golden_fib(n):
    return int((GOLDEN ** n - (1 - GOLDEN) ** n) / 5 ** 0.5)


def golden_fib_decimal(n):
    return Decimal(Decimal(Decimal(Decimal((Decimal(pow(Decimal(GOLDEN_D), Decimal(n))) - Decimal(pow(Decimal(1 - GOLDEN_D), Decimal(n))))) / 5) ** Decimal(0.5)))


# Вычисляет ближайшее приближение золотого сечения по номеру числа фибоначчи
def closed_golden(n):
    return golden_fib(n + 1) / golden_fib(n)


# вычисляет сумму чисел фибоначчи
def sum_fib(n):
    result = 0
    for i in range(0, n + 1):
        result += golden_fib(i)
    return result


def mean(n):
    return sum_fib(n) / (n + 1)


def variance_fib(n):
    variance = mean(n)
    result = 0
    for i in range(n + 1):
        result += (golden_fib(i) - variance) ** 2
    return result / (n + 1)


def mean_dev(n):
    variance = mean(n)
    result = 0
    for i in range(n + 1):
        result += abs(golden_fib(i) - variance)
    return result / (n + 1)
# 0 1 1 2 3 5 8 13 21   

def fib(n):
    first = 0
    second = 1
    third = first + second
    for i in range(n):
        first = second
        second = third
        third = first + second

    return third


if __name__ == '__main__':
    print(golden_fib(19))
    print(closed_golden(9))
    print(sum_fib(10))
    print(mean(9))
    print(variance_fib(9))
    print(mean_dev(9))
    print(golden_fib_decimal(4784971))
    print(fib(100000))
