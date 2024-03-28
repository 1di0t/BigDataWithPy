def polynominal(cs) ->str:
    """
    다항식 문자열을 히턴
    :param cs:계수들이 원소로 있는 리스트
    :return: 다항식 문자열 ex) f(x) = 5x^3-2x^2+0x^1+6x^0
    """
    poly = "f(x) = "
    exponent = len(cs) - 1
    for i in range(len(cs)):
        coef = cs[i]
        if coef >= 0 and i !=0:
            poly = poly + "+"

        poly = poly + str(coefficients) + "x^" + str(exponent) +" "
        exponent = exponent - 1
    return poly
    

coefficients = [5,-2,0,6]
print(polynominal(coefficients))