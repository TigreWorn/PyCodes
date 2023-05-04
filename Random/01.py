# def to_str(bytes_or_str):
#   if isinstance(bytes_or_str,bytes):
#     val=bytes_or_str.decode("utf-8")
#   else:
#     val=bytes_or_str
#   return val
# print(to_str("ok"))
# from urllib.parse import parse_qs as p
# myval= p('red=5&blue=9&green=',keep_blank_values=True)
# print(repr(myval))
n=int(input("enter num of times: "))
str=input("tell word boi")
for i in range(n):
  print(str)
