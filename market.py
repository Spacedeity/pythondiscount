def calculate_discount(price,discount_percentage) :
 
    if discount_percentage >= 20 :
        discount_amount = price * (discount_percentage/100 )
        final_price = price- discount_amount
        return final_price
    else :
        return price

myPrice =float(input("enter price :"))

discount_percentage = float(input("discount:"))

final_price=calculate_discount(myPrice,discount_percentage)

if discount_percentage >= 20 :

    print("your new price after discount:${final_price:.2f}")
else:
    print("low rate no discount was given.Price is:${:.2f}")



