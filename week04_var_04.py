def power(base, exponent) -> int:
    return base ** exponent
    pass

base = int(input("input number : "))
exponent = int(input("exponent number : "))
#
# result = 1
# for _ in range(exponent):
#     result = result * base
# print(f"{base}의 {exponent}제곱은 {result}")
# print(f"{base}의 {exponent}제곱은 {pow(base,exponent)}")
# print(f"{base}의 {exponent}제곱은 {base**exponent}")
print(f"{base}의 {exponent}제곱은 {power(base,exponent)}")