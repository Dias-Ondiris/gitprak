def calculate_delivery_cost(street_name, product_price):
    if "Аль-Фараби" in street_name or "Саина" in street_name or "Ташенова" in street_name or "Достык" in street_name:
        if product_price < 10000:
            return 500
        else:
            return 0
    else:
        if product_price < 10000:
            return 1000
        else:
            return 1000
street_name = "Аль-Фараби-Саина-Ташенова-Достык"
product_price = 8000

delivery_cost = calculate_delivery_cost(street_name, product_price)
print(delivery_cost) 
street_name = input()
product_price = int(input())
delivery_cost = calculate_delivery_cost(street_name, product_price)
print(delivery_cost)  