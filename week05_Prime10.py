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
empty =0

start, end= map(int,input("시작값 끝값 : ").split())
#start_end_Number = input("시작값 끝값 입력 : ").split()
for k in range(start,end):
        if is_prime(k) == True:
            print(k, end='\t')
            empty = empty + 1
        if empty == 20:
            print("\n")
            empty =0
