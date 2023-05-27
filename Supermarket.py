#!/usr/bin/env python
# coding: utf-8

# # CASE STUDY - HACKATHON

# In[ ]:


items = {
    1 : {"Item":"apple", 'Quantity':10,'cost':20},
    
    2 : {"Item":"orange", 'Quantity':10,'cost':10},
    
    3 : {"Item":"grapes", 'Quantity':15,'cost':30},
    
    4 : {"Item":"banana", 'Quantity':20,'cost':15},
    
    5 : {"Item":"watermelon", 'Quantity':5,'cost':40}}
def details():
    print('Welcome to Dear customer')
    print('\n Dear customer,fill your details.')
    print('--------------------------------------')
    name = input('\n Enter your name: ')
    address = input('\n Enter your adress/area name:')
    distance = int(input('\n Enter your distance from this mart(5/10/15/20): ' ))
    return name,address,distance

def materials():
    print('\n Items available in the cart')
    print('--------------------------------------------------------')
    print('%1s %15s %10s %20s' %('Sno','List of items','Quantity','Cost for each item'))

    print("%1s %10s %15d %10d"%('1',items[1]['Item'],items[1]['Quantity'],items[1]['cost']))
    print("%1s %10s %15d %10d"%('2',items[2]['Item'],items[2]['Quantity'],items[2]['cost']))
    print("%1s %10s %15d %10d"%('3',items[3]['Item'],items[3]['Quantity'],items[3]['cost']))    
    print("%1s %10s %15d %10d"%('4',items[4]['Item'],items[4]['Quantity'],items[4]['cost']))
    print("%1s %12s %13d %10d"%('5',items[5]['Item'],items[5]['Quantity'],items[5]['cost']))
    print('--------------------------------------------------------')
def tcost1():    
    a = int(input('\nHow many apples are you required?: '))
    o = int(input('\nHow many oranges are you required?: '))
    g = int(input('\nHow many grapes are you required?: '))
    b = int(input('\nHow many banana are you required?: '))
    w = int(input('\nHow many water melon are you required?: '))
    
   
    print('\n--------------------------BILL RECIEPT---------------------------------')
    print('Name:',name)
    print('\nAddress:',address)
    print('------------------------------------------------------------------------')
    print('Items bought in the cart')
    print('------------------------------------------------------------------------')
    print('%1s %15s %10s %10s %10s' %('\n Sno','List of items','Quantity','your Cost','Remaining items'))
    print('------------------------------------------------------------------------')
    print("%1s %10s %15d %10d %10d"%('1',items[1]['Item'],a,a*items[1]['cost'],10-a))
    print("%1s %10s %15d %10d %10d"%('2',items[2]['Item'],o,o*items[2]['cost'],10-o))
   
    print("%1s %10s %15d %10d %10d"%('3',items[3]['Item'],g,g*items[3]['cost'],15-g))    
    print("%1s %10s %15d %10d %10d"%('4',items[4]['Item'],b,b*items[4]['cost'],20-b))
    print("%1s %12s %13d %10d %10d"%('5',items[5]['Item'],w,w*items[5]['cost'],5-w))
    tcost =  a*items[1]['cost'] + o*items[2]['cost'] + g*items[3]['cost'] + b*items[4]['cost'] + w*items[5]['cost']
    print('------------------------------------------------------------------------')
    print()
    x=items[1]['Quantity'] - a
    y=items[2]['Quantity'] - o
    z=items[3]['Quantity'] - g
    m=items[4]['Quantity'] - b
    n=items[5]['Quantity'] - w
    
    items[1]['Quantity'] = x
    items[2]['Quantity'] = y
    items[3]['Quantity'] = z
    items[4]['Quantity'] = m
    items[5]['Quantity'] = n
    print('OVERALL BILL AMOUNT')
    return tcost

def delivery(distance,tcost):
    if distance > 0 and distance <= 5:
        delivery_charge = 10
        final_cost = tcost + delivery_charge
       
    elif distance > 5 and distance <= 10:
        delivery_charge = 12
        final_cost = tcost + delivery_charge
        
    elif distance > 10 and distance <= 15:
        delivery_charge = 14
        final_cost = tcost + delivery_charge
        
    else:
        delivery_charge = 20
        final_cost = tcost + delivery_charge
        
    print('-----------------------------------------------------------------------')
    print('%20s %20s %20s ' %('Total cost','Delivery cost','Final cost'))
    print('-----------------------------------------------------------------------')
    print('%15d %15d %20d ' %(tcost,delivery_charge,final_cost))
    
    return final_cost

while True:
    name,address,distance=details()
    materials()
    tcost = tcost1()
    delivery(distance,tcost)
    choose = input("\n Would you like to do shop again? (yes/no) ")
    if choose == 'no':
        print('\n---Thanks for your shopping...Have a nice day---')
        break
    else:
        continue


# In[ ]:




