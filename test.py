def add(a,b):
    return a + b

def sub(a, b):
    return a - b 

def mul(a, b): 
    return a * b

def div(a, b):
    return a / b
    

while True:
    print('1. Addition:')
    print('2. Subtraktion:')
    print('3. Multiplikation:')
    print('4. Division:')
    print('5, Avsluta programmet!')
    
    val = input('Välja vilket operation du vill göra!:\n')

    if val == '5': break
    a = float(input('a:'))
    b = float(input('b:'))

    if val == '1': print(add(a, b))
    elif val == '2': print(sub(a, b))
    elif val == '3': print(mul(a, b))
    elif val == '4': print(div(a, b))
        
