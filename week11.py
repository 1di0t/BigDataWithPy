def square_numbers(numbers,func):
    for number in numbers:
        print(func(number))

numbers = [i for i in range(1,11)]#list compreension
square_numbers(numbers,lambda number:number*number)