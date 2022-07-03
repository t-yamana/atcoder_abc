
import re

content = input()
pattern = '(0*)$'

trimed_content = re.sub(pattern, '', content)
reversed_content = trimed_content[::-1]

answer = 'Yes' if reversed_content == trimed_content else 'No'
print(answer)
