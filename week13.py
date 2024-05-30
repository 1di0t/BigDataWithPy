#Decorater
def document_it(f):
    def inner_function(*args):
        print(f"Function Name : {f.__name__}")
        print(f"위치 기반 리스트 : {args}")
        print(f"실행 결과 : {f(*args)}")
        return f(*args)
    return inner_function

def pow_ints(a,b):
    return pow(a,b)

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

new_is_prime = document_it(is_prime)
print(new_is_prime(7))

new_pow = document_it(pow)
print(new_pow(2,3))

new_add_ints = document_it(pow_ints)#pow_ints 함수를 수정하지 않고 새로운 함수로 만들어줌
print(new_add_ints(3,3))