from schema import MENU, resources
money=0

def check_resources(water, coffee, milk):
  if water > resources["water"] :
    print("Sorry there is not enough water.")
    return False
  elif coffee > resources["coffee"] :
    print("Sorry there is not enough coffee.")
    return False
  elif milk > resources["milk"] :
    print("Sorry there is not enough milk.")
    return False
  return True

def process_money(cost):
  print("Please insert coins...!!!")
  quarters = int(input("How many quarters ?"))
  dimes = int(input("How many dimes?"))
  nickles =  int(input("How many nickels?"))
  pennies =  int(input("How many pennies?"))

  total_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
  if(total_money >= cost):
    print(f"Here is {round(total_money - cost, 2)} dollars in change.")
    global money
    money += cost
    return True
  else:
    return False

def prepare_drink(water, coffee, milk):
  global resources
  resources["water"] -= water
  resources["coffee"] -= coffee
  resources["milk"] -= milk

def show_report():
  print(f'Water : {resources["water"]} ml')
  print(f'Milk : {resources["milk"]} ml')
  print(f'Coffee : {resources["coffee"]} g')
  print(f"Money : {money} ")


is_machine_on = True
while is_machine_on:
  coffee_type = input("What would you like? (espresso/latte/cappuccino):")
  if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino" :
    water = MENU[coffee_type]["ingredients"]["water"]
    coffee = MENU[coffee_type]["ingredients"]["coffee"]
    cost = MENU[coffee_type]["cost"]
    if coffee_type == "espresso":
      milk = 0
    else:
      milk = MENU[coffee_type]["ingredients"]["milk"]
  
    if check_resources(water, coffee, milk):
      if process_money(cost):
        prepare_drink(water, coffee, milk)
        print(f"Here is your {coffee_type}. Enjoy!")
      else:
        print("Sorry that's not enough money. Money refunded.")

  elif coffee_type == "report":
    show_report()

  elif coffee_type == "off" :
    print("Bye")
    is_machine_on = False

  else:
    continue
