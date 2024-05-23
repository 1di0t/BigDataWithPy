def out_func(i,j):#3,2 to this parameter
    def innerfunction(k,l):#get 3,2 in 4th line
        return  k*l
    return  innerfunction(i,j)#input 3,2

print(out_func(3,2))