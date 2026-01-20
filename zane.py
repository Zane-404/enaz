cat = []
total = []
#Drinks
drink = ['Green Tea','Malt Milk','Cream Milk','UHT Milk']
price1 = [3.00,2.85,3.50,4.15]
qnty1 = [0,0,0,0]
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
        print('---------------------------------------------------')
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
    combined_list = qnty1 + qnty2 + qnty3 + qnty4 + qnty5
    print(combined_list)
    x = 0
    for i in combined_list:
        x += i
    if x== 0:
        theclear()
        print('--------------------------------------------------------------------------------')
        print('CART')
        print('--------------------------------------------------------------------------------')
        print('the cart seems rather empty here...')
        choiceout = input('return to menu?[Y/N]?').lower()
        if choiceout == 'y':
            return
        else:
            print(checkout())

    else:
        theclear()
        print('--------------------------------------------------------------------------------')
        print('JUST_ORDER CART')
        print('--------------------------------------------------------------------------------')
        print('Items\t\t\tQuantity\tPrice/$\tTotal Price/$')
        y = 0
        for i in combined_list:
            if i>0:
                if y < 4:
                    item = drink[y]
                    price = price1[y] * i

                elif 4 <= y < 8:
                    item = Beer[y-4]
                    price = price2[y-4] * i

                elif 8 <= y < 12:
                    item = Frozen[y-8]
                    price = price3[y-8] * i

                elif 12 <= y < 16:
                    item = Household[y-12]
                    price = price4[y-12] * i
                
                else:
                    item = Snacks[y-16]
                    price = price5[y-16] * i
                
                item_width = 17
                item_display = item[:item_width]
                from decimal import Decimal
                price_individual = Decimal(price / i).quantize(Decimal('0.01'))
                price = Decimal(price).quantize(Decimal('0.01'))
                print(f'{item_display:<17}{i :>14}{price_individual:>15}{price:>10}')

                #adding to total list
                total.append(price)

            y += 1
        
        print('--------------------------------------------------------------------------------')
        total_sum = sum(total)
        print(f'Total Amount payable:${total_sum}')
        print('--------------------------------------------------------------------------------')
        PAYDAY = input('proceed to checkout?[Y/N}?:').lower()
        
    



    #asking for discount/membership


        

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