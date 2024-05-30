#Decorater
def document_it(f):
    def inner_function(*args):
        print(f"Function Name : {f.__name__}")
        print(f"위치 기반 리스트 : {args}")
        print(f"실행 결과 : {f(*args)}")
        return f(*args)
    return inner_function

def square_it(func):
    def inner_function(*args):
        result = func(*args)
        return result * result
    return inner_function

@square_it
@document_it
def pow_ints(a,b):
    return pow(a,b)

@document_it
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


new_pow = square_it(document_it(pow))
print(new_pow(2,4))