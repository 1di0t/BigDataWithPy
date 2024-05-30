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

new_add_ints = document_it(pow_ints)#pow_ints 함수를 수정하지 않고 새로운 함수로 만들어줌
print(new_add_ints(3,3))