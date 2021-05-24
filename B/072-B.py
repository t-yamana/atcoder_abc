
text = input()

'''Best Way'''
ans = text[0::2]

'''Way1'''
# odd_idx = range(len(text))[::2]
# ans = ''.join([text[i] for i in odd_idx])

'''Way2'''
# ans = ''
# for i, h in enumerate(text, 1):
#     if i % 2 == 1:
#         ans += h

print(ans)
