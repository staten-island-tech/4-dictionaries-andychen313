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
},

{
    "name": "Watermelon",
    "price": 4.29,
    "unit": "/lb",
    "description": "Watermelons have an elongated round shape with stripes in an unfixed pattern. Watermelons usually have a green color on the outside and have a red color on the inside."
},

{
    "name": "Dragonfruit",
    "price": 3.49,
    "unit" : "/lb",
    "description": "Dragonfruits have a unique shape and have a quite jagged figure. Dragonfruits usually have a reddish pink color on the outside. However, dragonfruits can have either a whitish or bloody pink color."
},

{
    "name": "Pineapple",
    "price": 2.49,
    "unit": "/lb",
    "description": "Pineapples have a cylindrical shape with a rough, spiky outer skin and green leaves on top. Its color is yellow on the inside. Pineapples are high in vitamin C and manganese, promoting healthy digestion and immune function."
},

{
    "name": "Mango",
    "price": 1.59,
    "unit": "/lb",
    "description": "Mangoes have an oval shape. Its skin color ranges from green to red and yellow, while the inside is orange. Mangoes are rich in vitamin C and vitamin A, supporting skin and eye health."
},

{
    "name": "Peach",
    "price": 2.19,
    "unit": "/lb",
    "description": "Peaches are round with a slightly fuzzy skin. Their color is a mix of orange, yellow, and red. Peaches are high in vitamin C and antioxidants, which support healthy skin and digestion."
},

{
    "name": "Pear",
    "price": 1.69,
    "unit": "/lb",
    "description": "Pears have a distinct oval shape that narrows near the stem. Their color can range from green to yellow or red. Pears are high in fiber and vitamin C, aiding in digestion and immune health."
},

{
    "name": "Grape",
    "price": 2.79,
    "unit": "/lb",
    "description": "Grapes are small and round. Their color can be green, red, or purple. Grapes are high in antioxidants, particularly resveratrol, which supports heart health."
},

{
    "name": "Cherry",
    "price": 3.59,
    "unit": "/lb",
    "description": "Cherries are small and round with a bright red or deep burgundy color. Cherries are rich in vitamin C and antioxidants, known to reduce inflammation and support sleep."
},

{
    "name": "Papaya",
    "price": 2.39,
    "unit": "/lb",
    "description": "Papayas have an elongated oval shape. Its outer skin is greenish-yellow, and the inside is orange with black seeds. Papayas are high in vitamin C and contain enzymes that aid digestion."
},

{
    "name": "Pomegranate",
    "price": 2.99,
    "unit": "/lb",
    "description": "Pomegranates are round with a hard red skin. Inside are juicy red seeds called arils. Pomegranates are high in antioxidants and vitamin C, promoting heart and skin health."
},

{
    "name": "Raspberry",
    "price": 3.19,
    "unit": "/lb",
    "description": "Raspberries are small, round clusters of drupelets. Their color is red or sometimes golden. Raspberries are high in fiber, vitamin C, and antioxidants, making them a nutritious fruit."
},

{
    "name": "Cantaloupe",
    "price": 1.99,
    "unit": "/lb",
    "description": "Cantaloupes are round with a rough tan skin and orange flesh inside. They are high in vitamin A and vitamin C, supporting eye health and hydration."
}

]

cart = []
total = 0.0


while True:
    print("Welcome to our market, where we sell multiple healthy fruits! These are the fruits we offer: ")
    for index, item in enumerate(market_items):
        print(index, ":", item["name"])

    
    choices = int(input("According to the index or the number that accomodates the fruit, what fruit would you like to add to your cart?: "))
    cart.append(market_items[choices]["name"])
    total += market_items[choices]["price"]

    continue_buying = input("Is that all? Would you like to buy more items? (Enter yes/no): ")
    if continue_buying != "yes":
        break


print("Your cart currently contains these following items: ")
for item in cart:
    print("-", item)
print(f"Total cost: ${total:.2f}")

