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
     