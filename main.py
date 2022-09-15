
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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


# TODO 2. Ability to print report


def print_report():
    for key, value in resources.items():
        print(key,':', value)
    return f'money : ${money}'


# TODO 1. Prompt option and display price
print('Coco\'s Coffee Machine')
print('Espresso: $1.50 | Latte: $2.50 | Cappuccino: $3.00')
drink_choice = input('\nWhat would you like today? (Espresso, Latte, Cappuccino): ').lower()


# TODO 3. Check if resources are sufficient


def resource_check(drink_choice):
    water_req = MENU[drink_choice]['ingredients']['water']
    milk_req = MENU[drink_choice]['ingredients']['milk']
    coffee_req = MENU[drink_choice]['ingredients']['coffee']

    water_available = resources['water']
    milk_available = resources['milk']
    coffee_available = resources['coffee']

    if water_available > water_req and milk_available > milk_req and coffee_available > coffee_req:
        return True
    else:
        return False


def resource_shortage(drink_choice):
    water_req = MENU[drink_choice]['ingredients']['water']
    milk_req = MENU[drink_choice]['ingredients']['milk']
    coffee_req = MENU[drink_choice]['ingredients']['coffee']

    water_available = resources['water']
    milk_available = resources['milk']
    coffee_available = resources['coffee']

    if water_available < water_req:
        return 'Sorry there is not enough water'
    elif milk_available < milk_req:
        return 'Sorry there is not enough milk'
    elif coffee_available < coffee_req:
        return 'Sorry there is not enough coffee'


def transaction_check(drink_choice, coin_total):
    drink_total = MENU[drink_choice]['cost']
    if coin_total > drink_total:
        money += drink_total
        change = coin_total - drink_total
        return f'Here is ${change} in change.'
    elif coin_total == drink_total:
        money += coin_total
    elif drink_total > coin_total:
        return f'Sorry, that is not enough money. Money refunded'
#
# if not resource_check:
#     print(resource_shortage(drink_choice))
#
#
# print(resource_check(drink_choice))
# print(resource_shortage(drink_choice))
# print(resource_check('latte'))
money = 0

# TODO 4. Ability to process coins
# if resource_check:
print('Your total is cost. Please insert coins')
num_of_quarters = int(input('How many quarters? '))
num_of_nickels = int(input('How many nickels? '))
num_of_dimes = int(input('How many dimes? '))
num_of_pennies = int(input('How many pennies? '))

coin_total = (num_of_quarters * 0.25) + (num_of_nickels * 0.05) + (num_of_dimes * 0.10) + (num_of_pennies * 0.01)

print(coin_total)
print(transaction_check(drink_choice, coin_total))



# TODO 5. Ability to check that transaction was successful

# TODO 6. Make coffee (deduct ingredients from resources)

# TODO 7. Ability to purchase another (loop)

# TODO 8. Turn off by entering off prompt
