def soldier(word):
    def innerfunction():
        return  f"{word} : 특공!"
    return  innerfunction
a = soldier("Sinper")
b = soldier("Ranger")
print(a())
print(b())