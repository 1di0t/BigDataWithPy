#from tkinter import * #GUI module
import tkinter as tk

def is_prime(k) -> bool:
    """
    :param k:소수인지 판별할 양의 수
    :return: If n is Prime :true, Not Prime : False
    """
    if k == 2:return True
    elif k <= 1 or k % 2 == 0:return False
    else:
        i = 2
        while i * i <= k:
            if k % i == 0:
                return False
            i = i + 1
        return True

def printPrime():
    number = int(en_input_number.get())
    text =""
    if is_prime(number): text = "소수"
    else: text = "소수가 아님"
    lab_print_prime_and_odd_even_num.config(text=f"\n{number}는 {text}\n")

def printOddEven():
    number = int(en_input_number.get())
    iseven = ""
    if number%2==0: iseven = "짝수"
    else : iseven = "홀수"
    lab_print_prime_and_odd_even_num.config(text=f"\n{number}는 {iseven}\n")

window = tk.Tk()
window.geometry("500x400")#Size
window.title("솟수")

en_input_number = tk.Entry(window)
lab_print_prime_and_odd_even_num = tk.Label(window,text="\n소수 판정 프로그램\n홀짝도 해줘용",border=2.4)
btn_prime_num = tk.Button(window,text="소수 판정",background="orange",border=2.4,command=printPrime)#함수의 이름만 입력 괄호는 포함하지 않는다
btn_odd_even_num = tk.Button(window,text="홀짝 판정",background="orange",border=2.4,command=printOddEven)



#placement
lab_print_prime_and_odd_even_num.grid(row=0,column=0,columnspan=2)
en_input_number.grid(row=1,column=0,columnspan=2)
btn_prime_num.grid(row=2,column=0,sticky="WE")
btn_odd_even_num.grid(row=2,column=1,sticky="WE")


window.mainloop()