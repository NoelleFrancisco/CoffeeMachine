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


def print_report():
    """Function to print report of current resources in machine"""
    for key, value in resources.items():
        print(key, ':', value)
    print(f'money : ${profit}')


def resource_check(order_ingredients):
    """Function to confirm if requested drink can be made based on available resources"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def transaction_check(drink_choice, coin_total):
    """Function to confirm if payment provided meets cost of drink"""
    drink_total = MENU[drink_choice]['cost']
    if coin_total > drink_total:
        return True
    elif coin_total == drink_total:
        return True
    elif drink_total > coin_total:
        return False


def calculate_change(drink_choice, coin_total):
    """Function to calculate if payment excess or shortage exists"""
    drink_total = MENU[drink_choice]['cost']
    if coin_total > drink_total:
        change = round(coin_total - drink_total, 2)
        print(f'Here is ${change} in change.')
        global profit
        profit += drink_total
        return True
    elif drink_total > coin_total:
        return f'Sorry, that is not enough money. Money refunded'


def payment():
    """Function to collect payment and calculate total"""
    total = 0
    print('Please insert coins:')
    total += int(input('How many quarters? ')) * 0.25
    total += int(input('How many nickels? ')) * 0.05
    total += int(input('How many dimes? ')) * 0.10
    total += int(input('How many pennies? ')) * 0.01
    return total


def make_coffee(choice, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    return f"Here is your {choice}. Enjoy!"


def start_machine():
    is_on = True
    while is_on:

        print('\nCoco\'s Coffee Machine')
        print('Espresso: $1.50 | Latte: $2.50 | Cappuccino: $3.00')
        choice = input('\nWhat would you like today? (Espresso, Latte, Cappuccino): ').lower()

        if choice == "off":
            print('Shut down process commence')
            return False
        elif choice == "report":
            print_report()
        else:
            drink = (MENU[choice])
            if resource_check(drink['ingredients']):
                coin_total = payment()
                calculate_change(choice, coin_total)
                print(make_coffee(choice, drink['ingredients']))


profit = 0

start_machine()
