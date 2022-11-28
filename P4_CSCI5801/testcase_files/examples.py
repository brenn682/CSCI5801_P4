def sum_list(vals):
  if len(vals) == 0:
     return 0
  else:
    return vals[0] + sum_list(vals[1:]) 
def reverse_string(st):
    if len(st) == 0:
       return st
    else:
       return reverse_string(st[1:]) + st[0]
def fibonacci(n):
    if n == 1:
      return 1
    elif n == 0:
      return 0 
    else:
      return fibonacci(n-1) + fibonacci(n-2)
def double_reverse(str_list):
    if len(str_list) == 0:
       return str_list
    else:
       var = double_reverse(str_list[:-1])
       var.insert(0, reverse_string(str_list[-1])) 
       return var
def deep_square(nested_list):
   if nested_list == []:
      return nested_list
   if type(nested_list[0]) == int:
      return [nested_list[0] ** 2] + deep_square(nested_list[1:])
   if type(nested_list[0]) == list:
      return [deep_square(nested_list[0])] + deep_square(nested_list[1:])
