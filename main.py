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
machine = CoffeeMaker()
machine.report()