
for Fahrenheit in range(-10,101,5):
    Celcius = 5/9*(Fahrenheit - 32) #reken celcius uit
    Celcius = round(Celcius,2)#rond celcius af op 2 decimalen
    if Celcius<0:
        print(Fahrenheit,"Fahrenheit is gelijk aan",Celcius,"Celcius, het vriest")
    else:
        print(Fahrenheit,"Fahrenheit is gelijk aan",Celcius,"Celcius, het vriest niet")