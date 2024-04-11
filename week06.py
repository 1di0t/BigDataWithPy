texts = "Pickachu ThunderBolt"

print(texts[9::2])
texts = texts.replace("ThunderBolt","Spark")#convert ThunderBolt to Spark
texts = "H"+texts[1:]
texts = texts.replace("c"," ",2)#convert 'c' to ' ' twice
print(texts)