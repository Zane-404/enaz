cat = []
No_items1 = []
No_items2 = []
No_items3 = []
No_items4 = []
No_items5 = []


#Drinks
drink = ['Neo Green Tea','Melo Chocolate Malt Milk','Very-Fair Full Cream Milk','Nirigold UHT Milk']
price1 = [3.00,2.85,3.50,4.15]
qnty1 = [5,0,0,0]
#Beer
Beer = ['Lion','Panda','Axe','Henekan']
price2 = [52.00,78.00,58.00,68.00]
qnty2 = [0,0,0,0]
#Frozen
Frozen = ['Pizza','Soup','Frozen Ready Meal','Some Cheese']
price3 = [6.95,5.15,4.12,5.6]
qnty3 = [0,0,0,0]
#Household
Household = ['Tissue','Towel','Tissue Rolls','Softener']
price4 = [9.50,5.85,7.50,9.85]
qnty4 = [0,0,0,0]
#Snacks
Snacks = ['Seaweed','Cracker','Cookie','Crackers']
price5 = [3.1,2.05,4.80,3.55]
qnty5 = [0,0,0,0]


def theclear():
    for i in range(50):
        print('\n')

# all menus
def menu():
    theclear()
    print('-------------------------------------------------')
    print('JUST_ORDER')
    print('-------------------------------------------------')
    print('Drinks[1]', 'Beer[2]', 'Frozen[3]', 'Household[4]', 'Snacks[5]')
    print('-------------------------------------------------')
    print('[6]View Cart')
    print('[7]Exit the program')


def menu1():
    while True:
        theclear()
        print('-------------------------------------------------')
        print('JUST_ORDER')
        print('-------------------------------------------------')
        for i in range(4):
            print(f'[{i + 1}] - {drink[i]} ${price1[i]}')
        print('-------------------------------------------------')
        choice1 = int(input('Select your option:'))
        if choice1 > 4:
            print('invalid option')
        else:
            try:
                qnty1[choice1-1] = int(input('Please choose an amount:'))
                print('saved successfully, returning you back to menu...')
                return
            except:
                print('please put an integer')

def menu2():
    while True:
        theclear()
        print('-------------------------------------------------')
        print('JUST_ORDER')
        print('-------------------------------------------------')
        for i in range(4):
            print(f'[{i + 1}] - {Beer[i]} ${price2[i]}')
        print('-------------------------------------------------')
        choice2 = int(input('Select your option:'))
        if choice2 > 4:
            print('invalid option')
        else:
            try:
                qnty2[choice2 - 1] = int(input('Please choose an amount:'))
                print('saved successfully, returning you back to menu...')
                return
            except:
                print('please put an integer')



def menu3():
    while True:
        theclear()
        print('-------------------------------------------------')
        print('JUST_ORDER')
        print('-------------------------------------------------')
        for i in range(4):
            print(f'[{i + 1}] - {Frozen[i]} ${price3[i]}')
        print('-------------------------------------------------')
        choice3 = int(input('Select your option:'))
        if choice3 > 4:
            print('invalid option')
        else:
            try:
                qnty3[choice3 - 1] = int(input('Please choose an amount:'))
                print('saved successfully, returning you back to menu...')
                return
            except:
                print('please put an integer')



def menu4():
    while True:
        theclear()
        print('-------------------------------------------------')
        print('JUST_ORDER')
        print('-------------------------------------------------')
        for i in range(4):
            print(f'[{i + 1}] - {Household[i]} ${price4[i]}')
        print('-------------------------------------------------')
        choice4 = int(input('Select your option:'))
        if choice4 > 4:
            print('invalid option')
        else:
            try:
                qnty4[choice4 - 1] = int(input('Please choose an amount:'))
                print('saved successfully, returning you back to menu...')
                return
            except:
                print('please put an integer')

def menu5():
    while True:
        theclear()
        print('-------------------------------------------------')
        print('JUST_ORDER')
        print('-------------------------------------------------')
        for i in range(4):
            print(f'[{i + 1}] - {Snacks[i]} ${price5[i]}')
        print('-------------------------------------------------')
        choice5 = int(input('Select your option:'))
        if choice5 > 4:
            print('invalid option')
        else:
            try:
                qnty5[choice5 - 1] = int(input('Please choose an amount:'))
                print('saved successfully, returning you back to menu...')
                return

            except:
                print('please put an integer')

#checkout(a) and math(b)
def checkout():
    combined_list = No_items1 + No_items2 + No_items3 + No_items4 + No_items5
    if len(combined_list) == 0:
        theclear()
        print('-------------------------------------------------')
        print('CART')
        print('-------------------------------------------------')
        print('the cart seems rather empty here...')
        choiceout = input('return to menu?[Y/N]?').lower()
        if choiceout == 'y':
            return
        else:
            print(checkout())

    else:
        theclear()
        print('-------------------------------------------------')
        print('CART')
        print('-------------------------------------------------')
        print('test')
        input('test')

#crux of the programme
while True:

    print(menu())
    cat = input('Enter a category:')

    if cat == '1':
        menu1()
    elif cat == '2':
        menu2()
    elif cat == '3':
        menu3()
    elif cat == '4':
        menu4()
    elif cat == '5':
        menu5()
    elif cat == '6':
        checkout()
    else:
        input('Thank you for using our service')