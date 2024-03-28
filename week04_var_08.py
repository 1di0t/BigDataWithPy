
dividend = int(input("input dividend : "))
divisor = int(input("input divisor : "))

print(f"{dividend} // {divisor} = {dividend//divisor}")
print(f"{dividend} % {divisor} = {dividend%divisor}")

print(f"{dividend} // {divisor} = {divmod(dividend,divisor)[0]}")
print(f"{dividend} % {divisor} = {divmod(dividend,divisor)[1]}")
#print(divmod(dividend,divisor))#if input is 11,5 output is (2,1)