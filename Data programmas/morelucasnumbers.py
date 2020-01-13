r = int(input("hoeveel begingetallen? ") or "2")
lucasNumbers = [float(input('begingetal '+str(i)+'? ')) for i in range(1,r+1)]
n = int(input('hoeveel nummers? ')) 

while len(lucasNumbers) < n:
	lucasNumbers.append(sum(lucasNumbers[-r:]))

roundedLucas = [round(x,2) for x in lucasNumbers]

print(roundedLucas)
