texts = input("input sentence : ")
if texts.isalnum():
    print(f"only alphabet and numeric!!")
else:
    print(f"there are another thing is in sentence besides alphabet and numeric")
# try:
#     if texts.index(finding_text) >= 0:
#         print(texts.index(finding_text))
# except ValueError:
#     print(f"입력하신 문장에서 {finding_text} 를 찾을 수 없습니다")
