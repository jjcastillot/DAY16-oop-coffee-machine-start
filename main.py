from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Main variables
master_power = 'on'
keep_working = True

#Main display
print("COFFEE MACHINE 3000")
print('''
    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \\
    |               | | |
    |               |_| |
 ___|             |\___/
/    \___________/    \\
\_____________________/
''')
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

coffee_maker.report()
money_machine.report()

while keep_working:
    options = menu.get_items()
    choice = input(f"What would you like today ({options})?").lower()
    if choice == 'off':
        keep_working = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif (choice == 'latte') or (choice == 'espresso') or (choice == 'cappuccino'):
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Please choose a valid option!!!")