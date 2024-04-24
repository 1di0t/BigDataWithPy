def is_prime(k) -> bool:
    """

    :param k:소수인지 판별할 양의 수
    :return: If n is Prime :true, Not Prime : False
    """
    if k == 2:
        return True
    elif k <= 1 or k % 2 == 0:
        return False
    else:
        i = 2
        while i * i <= k:
            if k % i == 0:
                return False
            i = i + 1
        return True

num1 = int(input("첫번째 숫자 입력 :\t"))
num2 = int(input("두번째 숫자 입력 :\t"))

for k in range(num1,num2+1):
        if is_prime(k) == True:print(k, end='\t')

