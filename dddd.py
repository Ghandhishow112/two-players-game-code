# import re 
# digital= ''' Mr.Brown
#              Mr. Smith
#              Mr. T
#              Mr Simpson
#               Brown.good@gmail.com    '''
# pattern= re.compile(r'Mr\.\s\w*')
# matches=pattern.finditer(digital)
# for match in matches:
    
#   print(match)
while True :
    a=input(("input a number "))
    try:
      number= int(a)
      print(number)
    except  :
      print('no')
    breakpoint