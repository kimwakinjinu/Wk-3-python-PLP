def calculate_discount  (price:int ,discount_percent: int):
    if discount_percent>=20:
        tprice=price * (1-(discount_percent * 0.01))
        print(tprice)
    else:
        print(price)
        
price =input("Please enter the price of the item:")

discount_percent =input("Please enter the percentage discount offered for the item: ")

calculate_discount(int (price),int(discount_percent))