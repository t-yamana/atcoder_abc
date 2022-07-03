# https://atcoder.jp/contests/abc249/tasks/abc249_b

sample = input()
unq_sample = ''.join(set(sample))

ch1 = len(sample) == len(unq_sample)
ch2 = False
ch3 = False

for c in sample:
  # ASCIIコード 大文字
  if 65 <= ord(c) and ord(c) <= 90:
    ch2 = True
  # ASCIIコード 小文字
  if 97 <= ord(c) and ord(c) <= 122:
    ch3 = True

if ch1 and ch2 and ch3:
  print('Yes')
else:
  print('No')
