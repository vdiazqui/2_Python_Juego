import random
numero = random.randint(0,99)
intento = int
print ("WELCOME! Let's play a game.")
print ("I am going to think of a number from 0 to 99, and you are going to try to guess it. Don't worry, I'll help you out if you need.")
print ("Ready? Let's start.")
while numero != intento:
    intento = int(input('Enter a number from 0 to 99: '))
    if intento >99 or intento <0:
        print ('It looks like you did not pay attention to me! Please read the instructions again... The number has to be between 0 and 99.')
    elif numero < intento:
        print ('Mhmm... that is too big. Try again!')
    elif numero > intento:
        print ('Mhmm... that is too small. Try again!')
    else:
        print ("GOOD JOB!:))) The numer I had in mind was indeed",numero)
        break 