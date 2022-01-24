off = False

resources = {
        "Water": 500,
        "Milk": 500,
        "Coffee": 500,
        "Money": 10
    }


while off == False:
    drink = input("What would you like? (espresso/latte/cappuccino): ")

    if(drink.lower() == "off"):
        off = True
    elif(drink.lower() == "report"):
        for resource in resources:
            print(str(resource) + ": " + str(resources[resource]))
    elif(drink.lower() == "refill"):
        resources = {
            "Water": 500,
            "Milk": 500,
            "Coffee": 500,
            "Money": 10
        }

    if(drink.lower() == "espresso"):
        resources["Water"] = resources["Water"] - 100
        resources["Milk"] = resources["Milk"] - 50
        resources["Coffee"] = resources["Coffee"] - 25
        cost = 2
        total = 0

        if(resources["Water"] < 100):
            print("Sorry, there is not enough water")
            resources = resources["Water"] + 100
        elif(resources["Milk"] < 50):
            print("Sorry, there is not enough milk")
            resources = resources["Milk"] + 50
        elif(resources["Coffee"] < 25):
            print("Sorry, there is not enough Coffee")
            resources = resources["Coffee"] + 25
        else:
            quarter = float(input("Insert quarters: ")) * 0.25
            dime = float(input("Insert dimes: ")) * 0.10
            nickle = float(input("Insert nickles: ")) * 0.05
            penny = float(input("Insert pennies: ")) * 0.01

            total += quarter + dime + nickle + penny

            if(total == cost):
                resources["Money"] = resources["Money"] + total
                print("Here is your espresso. Enjoy :D!")
            elif(total > cost):
                change = total - cost
                resources["Money"] = resources["Money"] + 2
                print(f"Here is your espresso. Enjoy :D! plus your change is {change}")
            elif(total < cost):
                print("Sorry that's not enough money. Money refunded")

    elif(drink.lower() == "latte"):
        resources["Water"] = resources["Water"] - 75
        resources["Milk"] = resources["Milk"] - 25
        resources["Coffee"] = resources["Coffee"] - 100
        cost = 5
        total = 0

        if (resources["Water"] < 100):
            print("Sorry, there is not enough water")
            resources = resources["Water"] + 100
        elif (resources["Milk"] < 50):
            print("Sorry, there is not enough milk")
            resources = resources["Milk"] + 50
        elif (resources["Coffee"] < 25):
            print("Sorry, there is not enough Coffee")
            resources = resources["Coffee"] + 25
        else:
            quarter = float(input("Insert quarters: ")) * 0.25
            dime = float(input("Insert dimes: ")) * 0.10
            nickle = float(input("Insert nickles: ")) * 0.05
            penny = float(input("Insert pennies: ")) * 0.01

            total += quarter + dime + nickle + penny

            if (total == cost):
                resources["Money"] = resources["Money"] + total
                print("Here is your espresso. Enjoy :D!")
            elif (total > cost):
                change = total - cost
                resources["Money"] = resources["Money"] + 5
                print(f"Here is your espresso. Enjoy :D! plus your change is {change}")
            elif (total < cost):
                print("Sorry that's not enough money. Money refunded")

    elif(drink.lower() == "cappuccino"):
        resources["Water"] = resources["Water"] - 150
        resources["Milk"] = resources["Milk"] - 10
        resources["Coffee"] = resources["Coffee"] - 50
        cost = 4
        total = 0

        if (resources["Water"] < 100):
            print("Sorry, there is not enough water")
            resources = resources["Water"] + 100
        elif (resources["Milk"] < 50):
            print("Sorry, there is not enough milk")
            resources = resources["Milk"] + 50
        elif (resources["Coffee"] < 25):
            print("Sorry, there is not enough Coffee")
            resources = resources["Coffee"] + 25
        else:
            quarter = float(input("Insert quarters: ")) * 0.25
            dime = float(input("Insert dimes: ")) * 0.10
            nickle = float(input("Insert nickles: ")) * 0.05
            penny = float(input("Insert pennies: ")) * 0.01

            total += quarter + dime + nickle + penny

            if (total == cost):
                resources["Money"] = resources["Money"] + total
                print("Here is your espresso. Enjoy :D!")
            elif (total > cost):
                change = total - cost
                resources["Money"] = resources["Money"] + 4
                print(f"Here is your espresso. Enjoy :D! plus your change is {change}")
            elif (total < cost):
                print("Sorry that's not enough money. Money refunded")