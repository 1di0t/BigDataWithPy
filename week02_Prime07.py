num1 = int(input("첫번째 숫자 입력"))
num2 = int(input("두번째 숫자 입력"))


for k in range(num1,num2+1):
    is_prime_num = True

    if k<2 or k%2==0:
        is_prime_num = False
    else:
        i=2
        while i*i <= k:
            if k % i ==0:
                is_prime_num = False
                break;
            i = i+1
        if is_prime_num == True:
            print(k + "\n")

