import math
import datetime


def vindpriem(zoekpriem):  # deze functie kijkt of een bepaald getal priem is door te kijken of het deelbaar is door voorgaande priemgetallen
    for primeNumber in primeNumbers:
        # het is niet nodig om verder te kijken dan de wortel van een priemgetal, dus gaat ie op dat moment uit de functie
        if primeNumber > math.ceil(math.sqrt(zoekpriem)):
            return True
        if zoekpriem % primeNumber == 0:
            return False


start = int(input('vanaf welk getal wil je de priemgetallen hebben? '))
finish = int(input('tot welk getal wil je de priemgetallen hebben? '))
primeNumbers = [5]

i = max(primeNumbers)
t1 = datetime.datetime.now()
while i < finish:
    i += 2
    if vindpriem(i):
        primeNumbers.append(i)
    i += 4
    if vindpriem(i):
        primeNumbers.append(i)

primeNumbers = [2, 3] + primeNumbers
displayprimes = [x for x in primeNumbers if x <= finish and x >= start]
t2 = datetime.datetime.now()
print(displayprimes)
print(len(displayprimes))
print(t2-t1)
