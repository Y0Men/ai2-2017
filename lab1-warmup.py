def helloworld():
    print("Hello, world!")

def board():
    a = '|'.join(['  ']*3)
    b = '\n{}\n'.format('-'*8)
    print(a,a,a,sep=b)
    
def tictactoe():
    a = 'H'.join(['  |  |  ']*3) + '\n'
    b ='H'.join(['--+--+--']*3) + '\n'
    c = a.join([b]*3)
    separator = '+'.join(['='*8]*3) + '\n'
    print(c,c,c,sep=separator)

def multiples():
    for i in range (0,1002):
        if i%5==0:
            print(i,end=' ')
        elif i%3==0:
            print(i,end=' ')
        i=i+1

def collatz(number):
    if number%2==0:
        print(number, "->", end=' '),
        number=number/2        
        collatz(number)
    elif number%2==1:
        if number==1:
            print(number)
        else:
            print(number, "->", end=' '),
            number=3*number+1            
            collatz(number)

def ftoc(temp):
    celsius = (temp - 32) * (5/9)
    print(celsius)
    
board();
tictactoe()
multiples()
collatz(44)
ftoc(66)