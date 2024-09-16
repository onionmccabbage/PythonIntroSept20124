#review game by Alessandro Inghilterra
from random import randint
numtry = 0
guess = False
mynum = randint(0,100)

def makeInt(nn):
    n=int(float(nn))
    return n

while guess is False:
      numtry = numtry+1
      nn = input('Guess my number.... : ')
      n = makeInt(nn)
      if n<mynum:
            print(f'{n} is too low, please retry')
      elif n>mynum:
            print(f'{n} is too high, please retry')
      elif n==-1:
            print(f'Game over :( )')
            break      
      else:
            print(f'Well done, {mynum} is the correct number and you got it into {numtry} times')
            guess = True