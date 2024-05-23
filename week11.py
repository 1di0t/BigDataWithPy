def printAplusB(a,b):
    print(a+b)
def is_prime(k) -> bool:
    """

    :param k:소수인지 판별할 양의 수
    :return: If n is Prime :true, Not Prime : False
    """
    is_prime_num = True
    if k < 2 or k % 2 == 0:
        return False
    else:
        i = 2
        while i * i <= k:
            if k % i == 0:
                return False
            i = i + 1
        return True

def prime(func,num):
    print(func(num))

prime(is_prime,24)
print(list(map(abs,[1,5,-7,20,-30])))#iterable
print(list(map(is_prime,[1,5,-7,20,-30])))