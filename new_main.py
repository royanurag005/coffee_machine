import time
import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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
cost_items={'espresso' : 1.5,
            'latte' : 2.5,
            "cappuccino" : 3.0}
COFFEE_MACHINE={"water" : 300 ,
                "milk" : 200,
                "coffee" : 100
                }
# print(MENU["cappuccino"]["cost"])
# TODO : 1 . Print report of all coffee machine resources
def resources_available():
    print(f"Water available in the machine is : {COFFEE_MACHINE['water']} .")
    print(f"Milk available in the machine is : {COFFEE_MACHINE['milk']} .")
    print(f"Coffee available in the machine is : {COFFEE_MACHINE['coffee']} .")


def sum_coins(p, n, d, q):
    total = (p*0.01)+(n*0.05)+(d*0.10)+(q*0.25)
    return total
sum_money=0
def money(demand):
    stimulus='none'
    if (COFFEE_MACHINE['water'] < MENU[demand]['ingredients']['water']):
        stimulus='water'
    elif(COFFEE_MACHINE['milk'] < MENU[demand]['ingredients']['milk']):
        stimulus='milk'
    elif(COFFEE_MACHINE['coffee']<MENU[demand]['ingredients']['coffee']):
        stimulus='coffee'
    else:
        stimulus='power'

    if(COFFEE_MACHINE['water']>=MENU[demand]['ingredients']['water'] and COFFEE_MACHINE['milk']>=MENU[demand]['ingredients']['milk'] and COFFEE_MACHINE['coffee']>=MENU[demand]['ingredients']['coffee']):
        print("Please insert coins .")
        quarter=int(input("how many quarters?:"))
        dimes=int(input("how many dimes?: "))
        nickles=int(input("how many nickles?:"))
        penny=int(input("how many pennies?: "))
        global sum_money
        sum_money+=cost_items[demand]

        total=sum_coins(penny,nickles,dimes,quarter)
        if(total>cost_items[demand]):
            # value=sum_coins(penny,nickles,dimes,quarter)
            # print(value)
            # print(total)
            ret_money=total - cost_items[demand]
            return_money=round(total - cost_items[demand],2)
            print(f"Here is ${return_money} in change. ")
            print(f"Here is your {demand} ☕ .")
            COFFEE_MACHINE['water']-=MENU[demand]['ingredients']['water']
            COFFEE_MACHINE['milk']-=MENU[demand]['ingredients']['milk']
            COFFEE_MACHINE['coffee']-=MENU[demand]['ingredients']['coffee']

        else:
            print("""Sorry that's not enough money. Money refunded.""")
    else:
        print(f"Sorry there is not enough {stimulus} .")

def user_input():
    demand=input("What would you like ? (espresso/latte/cappuccino)\n").lower()
    return demand

# while(COFFEE_MACHINE['water']<)
to_continue=True
while(to_continue):
    print(f"Espresso costs : ${cost_items['espresso']}.")
    print(f"Latte costs : ${cost_items['latte']}.")
    print(f"Cappuccino costs : ${cost_items['cappuccino']}.")
    time.sleep(5)
    resources_available()
    os.system('cls')
    x=user_input()
    if(x=='off'):
        to_continue=False
    else:
        money(x)
        print(f"The money in cash available in the machine is : ${sum_money} .")
print("Thank You!!!")
