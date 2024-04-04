def polynominal(cs) -> str:
    """
    다항식 문자열을 히턴
    :param cs:계수들이 원소로 있는 리스트
    :return: 다항식 문자열 ex) f(x) = 5x^3-2x^2+0x^1+6x^0
    """
    poly = "f(x) = "
    exponent = len(cs) - 1
    for i in range(len(cs)):
        coef = cs[i]
        if coef >= 0 and i != 0:
            poly = poly + "+"
        poly = poly + str(coef) + "x^" + str(exponent) + " "
        exponent = exponent - 1
    return poly


def calculate_polynominal(x, cs) -> int:
    """
    calculate polynominal and return result
    :param x: integer input
    :param cs: integer list
    :return: integer result
    """
    result = 0
    exponent = len(cs) -1
    for i in range(len(cs)):
        coefficient = cs[i]
        result = result + coefficient*pow(x,exponent)
        exponent = exponent - 1
    return result


coefficients = [2, 1]
print(polynominal(coefficients))
x = int(input("x값을 입력하세요 : "))
print(calculate_polynominal(x,coefficients))
