import random
def megaMillion():
  megaNumber = 0
  oneOfFive = 0
  print("Your 5 'Mega Millions' numbers are:  " + "\n")
  for i in range(5):
    oneOfFive = random.randrange(1, 71)
    print(oneOfFive)
    #print('\n')
  megaNumber = random.randrange(1, 26)
  print("And the Mega number is: ")
  print(megaNumber)

def powerBall():
  megaNumber = 0
  oneOfFive = 0
  print("Your 5 'Power Ball' numbers are:  ")
  for i in range(5):
    oneOfFive = random.randrange(1, 70)
    print(oneOfFive)
    #print('\n')
  megaNumber = random.randrange(1, 27)
  print("And the Mega number is: ")
  print(megaNumber)

def superLotto():
  megaNumber = 0
  oneOfFive = 0
  print("Your 5 'Super Lotto' numbers are:  ")
  for i in range(5):
    oneOfFive = random.randrange(1, 48)
    print(oneOfFive)
    #print('\n')
  megaNumber = random.randrange(1, 28)
  print(" And the Mega number is: ")
  print(megaNumber)

def main():
    try:
        uInp = raw_input('What game you playing? mega, power, super? ')
        while uInp.lower() != 'no':
            if uInp.lower() == 'mega':
                megaMillion()
            elif uInp.lower() == 'power':
                powerBall()
            elif uInp.lower() == 'super':
                superLotto()
            else:
                print("invalid input")
            uInp = raw_input("Type 'NO' if you don't want to play again, or type mega or power or super: ")
        print('Bye-bye, see you next time')


    except Exception as e:
        print('error error error')
        print(e)

if __name__ == '__main__':
  main()

