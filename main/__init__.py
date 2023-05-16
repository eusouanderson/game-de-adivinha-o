from random import randint



def numbers(num):
    numale = str(randint(1, 5))
    if num == numale:
        
        return(f'Numero Correto! O numero escolhido pelo programa foi {numale}')
    else:
        return(f'Numero Errado! O numero escolhido pelo programa foi {numale}')
    

