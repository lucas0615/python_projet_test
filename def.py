
#定義Function
def function():
    print('This is a function')
    a=1+2
    print(a)

def multiply(a, b):
    c = a * b
    print('The c is', c)
    
#函數默認    
def sale_car(price, brand, color = 'red', is_second_hand = True):
    print('price:', price,
          'color:', color,
          'brand:', brand,
          'is_second_hand:', is_second_hand)
    
def fun():
    a = 10
    print(a)
    return a+100
    
#使用定義好的Function    
function()
multiply(5,2)
sale_car(200000, 'BMW', color = 'blue')
print(fun())