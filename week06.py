texts = input("input sentence : ")
finding_text = input("input finding text : ")
if texts.find(finding_text) == -1:
    print(f"입력하신 문장에서 {finding_text} 를 찾을 수 없습니다")
try:
    if texts.index(finding_text) >= 0:
        print(texts.index(finding_text))
except ValueError:
    print(f"입력하신 문장에서 {finding_text} 를 찾을 수 없습니다")
#texts = "pikachu used ThunderBolt and died??!pikachu"

# print(texts.find("pikachu"))#start at 0
# print(texts.rfind("pikachu"))#start at end of texts
# print(texts.rfind("daelim"))#return -1
# print(texts.index("daelim"))#Value Error