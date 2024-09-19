print ('This code can find the total cost of your item after sales tax in maryland')

#user inputs the value of their item and stores it into a varibale 
subtotal = float(input("what's the price of your item?"))

#Multiply the subototal by 1.06 to get the total cost after maryland taxes
total = subtotal * 1.06

#Output the total
if total >= 0:
    print(f"your total after maryland sales tax is: ${total:.2f}")
else:
    print("your price cant be a negative number!!")
