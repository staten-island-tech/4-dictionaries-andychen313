market_items = [

{
    "name": "Apple",
    "price": 1.97,
    "unit": "/lb",
    "description": "This fruit is quite round. Its color is red. Apples are high in fiber and vitamin C, making it a healthy fruit option." 
},

{
    "name": "Banana",
    "price": 0.99,
    "unit": "/lb",
    "description": "This fruit has a quite of a curved shape. Its color is usually yellow, but it can also sometimes be a bright green. Bananas are high in potassium, making it a healthy fruit option."
},

{
    "name": "Orange",
    "price": 1.79,
    "unit": "/lb",
    "description": "This fruit is quite round. Its color is orange. Oranges are high in vitamin C, making it a healthy fruit option."
},

{
    "name": "Kiwi",
    "price": 1.89,
    "unit": "/lb",
    "description": "Kiwis have an oval shape. Kiwis have a brown skin on the outside but a green color on the inside. Kiwis are high in vitamin C and can benefit human skin and the digestive system, making it a healthy fruit option."
},

{
    "name": "Lemon",
    "price": 1.89,
    "unit": "/lb",
    "description": "Lemons have an oval shape. Its color is yellow. Lemons are high in vitamin C, benefits human skin, the digestive system, and the immune system, making it a healthy fruit option."
},

{
    "name": "Lime",
    "price": 1.29,
    "unit": "/lb",
    "description": "Limes have an oval shape. Its color is green. Limes are high in vitamin C. Limes also benefit the immune system and digestive system, which makes it a healthy fruit option."
},

{
    "name": "Strawberry",
    "price": 3.29,
    "unit": "/lb",
    "description": "Strawberries have a somewhat triangular shape. Its color is red. Strawberries are high in vitamin C and fiber."
},

{
    "name": "Blueberry",
    "price": 2.89,
    "unit": "/lb",
    "description": "Blueberries are round. Its color is a darkish blue. Blueberries are high in vitamin C, vitamin K, and manganese."
}

]

cart = []
total = 0.0


while True:
    print("Welcome to our market, where we sell multiple healthy fruits! These are the fruits we offer: ")
    for index, item in enumerate(market_items):
        print(index, ":", item["name"])

    
    choices = int(input("According to the index or the number that accomodates the fruit, what fruits(s) would you like to add to your cart?: "))
    cart.append(market_items[choices]["name"])
    total += market_items[choices]["price"]

    continue_buying = input("Is that all? Would you like to buy more items? (Enter yes/no): ")
    if continue_buying != "yes":
        break


print("Your cart currently contains these following items: ")
for item in cart:
    print("-", item)
print(f"Total cost: ${total:.2f}")