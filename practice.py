### Change calculator project ####
# Change Calculator
# Imagine that your friend is a cashier, 
# but has a hard time counting back change to customers.
# Create a program that allows him to input a certain
#  amount of change, and then print how many 
# quarters, dimes, nickels, and pennies are needed to
#  make up the amount needed. Example: if he inputs 
# 1.47, the program will say that he needs
#  5 quarters, 2 dimes, 0 nickels, and 2 pennies.
# Subgoals:
# So your friend doesn't have to calculate how much
#  change is needed, allow him to type in the amount
#  of money given to him and the price of the item. The
#  program should then tell him the amount
#  of each coin he needs like usual.
# To make the program even easier to use, loop the
#  program back to the top so your friend can continue
#  to use the program without having to close and
#  open it every time he needs to count change


import math
while True :
    
     x=input(("money in dollars: "))
     x=float(x)
     # q stands for quarters , d stands for dime , n stands for nickel and p stand for pennies 
     #(all values are in dollar equivalent)
     q=0.25
     d=0.1
     n=0.05
     p=0.01

     number_q= x/q
     numberQ=int(number_q)
     money2= round(x- (numberQ * q) , 2)
     number_d= money2/d
     numberD= int(number_d)
     money3= round(money2- (numberD *d), 2)
     number_n= money3/n
     numberN= int(number_n)
     money4= round(money3- (numberN *n),2)
     number_p= money4/p
     numberP= int(number_p)
     

     print(f'The change of {x} dollars is  \n{numberQ} quaters , {numberD} dimes , {numberN} nickles , and {numberP} pennies')
     breakpoint
     