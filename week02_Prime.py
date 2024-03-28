# import math
#
#
#
# def isPrime(number):
#     if number<2 or number%2==0:
#         return False
#     if number == 2:
#         return True
#     for i in range(3,int(math.sqrt(number)+1),2):
#         if number % i == 0:
#             return False
#         else:
#             return True
#
# num = int(input("숫자 입력"))
# if isPrime(num):
#     print("소수")
# else :
#     print("아님")

num = int(input("숫자 입력"))
is_prime_num = True

if num<2 or num%2==0:
    is_prime_num = False
if num%2==0:
    is_prime_num =True
else:
    for i in range(3,num,2):
        if num % i ==0:
            is_prime_num = False
            break;
        print(i, end="\n")
            
if is_prime_num == True:
    print("소수")
else:
    print("소수 아님")