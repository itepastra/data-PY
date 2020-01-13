lucasNumbers = [float(input("beginwaarde 1? ")),
                float(input("beginwaarde 2? "))]
n = int(input('hoeveel nummers? '))

for i in range(n):
    lucasNumbers.append(lucasNumbers[-1]+lucasNumbers[-2])

roundedLucas = [round(x, 2) for x in lucasNumbers]

print(roundedLucas)
