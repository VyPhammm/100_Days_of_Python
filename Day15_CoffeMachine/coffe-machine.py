MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def check_resources(option) :
    if MENU[option]["ingredients"]["water"] <= resources["water"] and MENU[option]["ingredients"]["milk"] <= resources["milk"] and MENU[option]["ingredients"]["coffee"] <= resources["coffee"] :
        resources["water"] = resources["water"] - MENU[option]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[option]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[option]["ingredients"]["coffee"]
        return True
    elif MENU[option]["ingredients"]["water"] > resources["water"] :
        print("Sorry there is not enough water.")
        return False
    elif MENU[option]["ingredients"]["milk"] <= resources["milk"] :
        print("Sorry there is not enough milk.")
        return False
    elif MENU[option]["ingredients"]["coffee"] <= resources["coffee"] :
        print("Sorry there is not enough coffee.")
        return False


def insert_coin() :
    print('Please insert coins.')
    total = int(input('How many quarters (1 quarters = $0.25) ?: ')) * 0.25
    total += int(input('How many dimes (1 dimes = $0.10) ?: ')) * 0.1
    total += int(input('How many nickles (1 nickles = $0.05) ?: ')) * 0.05
    total += int(input('How many pennies (1 pennies = $0.01) ?: ')) * 0.01
    return total 
    

def check_money(total, cost) :  
    global money
    if total >= cost :
        refund = round(total - cost, 2)
        money += cost  
        print(f"Here is ${refund} in change")    
        return True
    else :
        print("Sorry that's not enough money. Money refunded")
        return False


def coffee_machine() :
    is_on = True
    while is_on :
        option = input(f"What would you like ? (espresso ({MENU['espresso']['cost']}) / latte ({MENU['latte']['cost']}) / cappuccino ({MENU['cappuccino']['cost']}): ").lower()        
        if option == "off" :
            is_on = False
        elif option == "report" :
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        else :
            status = check_resources(option=option)
            if status :
                payment = insert_coin()
                cost = MENU[option]['cost']
                check_money(total = payment, cost = cost)              
                print(f"Here is your {option} ☕. Enjoy!")
            else :
                is_on = False

# payment = insert_coin()
# print(payment)

coffee_machine()












