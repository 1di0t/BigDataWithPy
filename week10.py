import tkinter as tk

w = tk.Tk()
w.geometry("200x300")
w.title("그리두")

btn_00 = tk.Button(w,text="00")
btn_01 = tk.Button(w,text="01")
btn_02 = tk.Button(w,text="02")

btn_10 = tk.Button(w,text="10")
btn_11 = tk.Button(w,text="11")
btn_12 = tk.Button(w,text="12")


btn_20 = tk.Button(w,text="20")
btn_21 = tk.Button(w,text="21")
btn_22 = tk.Button(w,text="22")


btn_00.grid(row=0,column=0)
btn_01.grid(row=0,column=1)
btn_02.grid(row=0,column=2,rowspan=3,sticky="NS")#NorthSouth

btn_10.grid(row=1,column=0)
btn_11.grid(row=1,column=1)
#btn_12.grid(row=1,column=2)

btn_20.grid(row=2,column=0,columnspan=2,sticky="WE")
#btn_21.grid(row=2,column=1)
#btn_22.grid(row=2,column=2)


w.mainloop()
