
text = input()
print(text[:1], text.rfind(text[-1:])-1, text[-1:], sep='')

# 他の回答
# print(text[0] + str(len(text)-2) + text[-1])
