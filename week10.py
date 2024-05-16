#from tkinter import * #GUI module
import tkinter as tk

window = tk.Tk()
window.geometry("500x200")#Size
window.title("솟수")

en_input_number = tk.Entry(window)
lab_print_prime_num = tk.Label(window,text="소수 판정 프로그램",border=2.4)
btn_prime_num = tk.Button(window,text="소수 판정",background="orange",border=2.4)

#placement
lab_print_prime_num.pack()
en_input_number.pack(fill='x')
btn_prime_num.pack(fill='x')



window.mainloop()