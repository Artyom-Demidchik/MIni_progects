menu = {'Drinkables': ['Coffee', 'Tea', 'Juise'],
        'Bakery': ['Croissant', 'Donut', 'Cake'],
        'Desserts': ['Ice_cream', 'Tiramisu', 'Marshmallows']}
selection_menu = {1: menu['Drinkables'],
                  2: menu['Bakery'],
                  3: menu['Desserts']}
order = []
exceptions = [['yes', 'Yes', 'YES'], ['no', 'No', 'NO']]
print('We welcome you to our cafeteria!', end='\n' * 2)
answer = input('Want to place an order? -> ')
print()
while (answer not in exceptions[0]) and (answer not in exceptions[1]):
    print('Incorrect answer! Please try again...')
    answer = input('Want to place an order? -> ')
    print()
if answer in exceptions[0]:
    while answer in exceptions[0]:
        print("Ok, what would you like to order?")
        proposed_choice = []
        position = 0
        variant = 0
        for i in menu:
            variant += 1
            print(str(variant) + '.', i)
        print()
        answer2 = int(input('Your choice -> '))
        print()
        while answer2 < 1 or answer2 > 3:
            print('Incorrect answer! Please try again...', end='\n' * 2)
            answer2 = int(input('Your choice -> '))
            print()
        print('Okay we have:')
        variant = 0
        for i in selection_menu[answer2]:
            variant += 1
            print(str(variant) + '.', i)
            proposed_choice.append(i)
        print('What do you choose?')
        answer3 = int(input('Your choice -> '))
        order.append([proposed_choice[answer3 - 1]])
        print('How many?')
        answer4 = int(input('Quantity -> '))
        order[position].append(proposed_choice[answer3 - 1])
        answer = input('Something else? -> ')
        while answer not in exceptions[0] or answer not in exceptions[1]:
            print('Incorrect answer! Please try again...')
            answer = input('Something else? -> ')
    print('Ok, your order is:')
    print(order)
elif answer in exceptions[1]:
    print('Then we wish you all the best!!! Goodbye')
