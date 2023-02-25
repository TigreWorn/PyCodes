# import re
# s = re.findall(f"[A-Za-z0-9]",input())
# if s:
#     print(s[0])
# else:
#     print(-1)

#You are given a string .
#Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.
import re
s = re.findall(r"([A-Za-z0-9])\1+",input())
if s:
    print(s[0])
else:
    print(-1)
