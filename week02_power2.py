base = int(input("input number : "))
exponent = int(input("exponent number : "))
print(f"{base}의 {exponent}제곱은 {pow(base,exponent)}")
result = 1
for i in range(exponent):
    result = result * base
print(f"{base}의 {exponent}제곱은 {result}")