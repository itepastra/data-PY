# Dit script maakt een aantal contourplots van de vectorpotentiaal ten gevolge van geladen deeltjes en slaat deze op in diverse plaatjes
# dit script is geschreven door Tijs Aarts en Victor Schyns op 22-11-2019


import numpy as np
import matplotlib.pyplot as plt


# deze functie neemt een verschil in x,y,z en berekent de coulombpotentiaal in dat punt
def V(deltax, deltay=0, deltaz=0, q=1):
    return q / (np.sqrt(deltax**2 + deltay**2 + deltaz**2))

# deze functie kan heel veel inputs ontvangen en maakt hiermee een plot


def maakplot(deeltjesx=np.array([]), deeltjesy=np.array([]), deeltjesz=np.array([]), deeltjesq=np.array([]), domein=[-1, 1, -1, 1], z=[0], naam='maakplot', titel='titel', contourhoogtes=15, nrows=1, ncols=1):
    x = np.linspace(domein[0], domein[1], 400)
    y = np.linspace(domein[2], domein[3], 400)
    X, Y = np.meshgrid(x, y)

    fig = plt.figure(naam, figsize=(6*ncols, 4*nrows))
    # ik zorg dat er een lege lijst is met een lang genoege lengte om alle subplots te gaan bevatten zodat mijn for loop goed werkt
    ax = [0 for i in range(nrows*ncols)]
    # print(ax)

    # hier tel ik de waarden van V voor elk punt voor elk deeltje op waardoor ik voor elk punt de coulombpotentiaal krijg in een 2D numpy array
    for p, j in enumerate(z):
        v = sum([V(X - deeltjesx[i], Y - deeltjesy[i], j - deeltjesz[i], deeltjesq[i])
                 for i in range(len(deeltjesx))])
        #print(p, ax[p])
        ax[p] = fig.add_subplot(nrows, ncols, p+1)
        cmap = ax[p].contour(X, Y, v, levels=contourhoogtes)
        ax[p].axis('scaled')
        ax[p].set_ylabel('$y$')
        ax[p].set_xlabel('$x$')
        ax[p].set_title('z = '+str(j), loc='left')
        cbar = fig.colorbar(cmap)
        cbar.set_label('kleuren bij V')

    plt.axis(domein)
    plt.suptitle(titel)
    plt.savefig(naam, bbox_inches='tight', format='png')


############## opdracht 1 ##############
q = 1
r = np.linspace(0, 1, 1000)[1:]
# ik pak r in de x-richting om de funcie V te kunnen gebruiken


fig1, [ax1, ax2] = plt.subplots(
    1, 2, False, False, num='opdracht 1', figsize=(16, 9), dpi=100)

color = 'tab:red'
ax1.set_xlabel('$r$')
ax1.set_ylabel('$V/q$', color=color)
# ik maak de y-as hier lineair (dit is niet nodig maar wel leesbaarder)
ax1.set_yscale('linear')
ax1.tick_params(axis='y', labelcolor=color)
ax1.tick_params(axis='x', labelcolor=color)
ax1.set_title('lineaire grafiek')
# ik roep hier de functie aan die ik in r5 heb gedefinieerd voor consistency
ax1.plot(r, V(r, 0, 0, 1), color=color)

color = 'tab:blue'
ax2.set_xlabel('$r$')
ax2.set_yscale('log')  # hier maak ik de as logaritmisch
ax2.tick_params(axis="y", labelcolor=color)
ax2.tick_params(axis="x", labelcolor=color)
ax2.set_title('logaritmische grafiek')
# hier doe ik hetzelfde als in regel 20
ax2.plot(r, V(r, 0, 0, 1), color=color)

plt.savefig('opdracht 1')
print('opdracht 1 klaar')

############## opdracht 2 ##############

deeltjex = [0]
deeltjey = [0]
deeltjez = [1]
deeltjeq = [1]
domein = [-1, 1, -1, 1]
z = [0]
naam = 'opdracht 2'
titel = 'coulombpotentiaal met een geladen deeltje op z = 1'
maakplot(deeltjex, deeltjey, deeltjez, deeltjeq, domein, z, naam, titel)
print('opdracht 2 klaar')

############## opdracht 3 ##############
# ik heb een library gemaakt die het coulombpotentiaal van elk aantal deeltjes in 3D kan uitrekenen,
# hier zet ik de waarden van de deeltjes van de kubus in variabelen voor overzicht voordat ik het in de functie doe
deeltjesx = [-0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5]
deeltjesy = [-0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5]
deeltjesz = [0.5, 0.5, 0.5, 0.5, -0.5, -0.5, -0.5, -0.5]
deeltjesq = [1, 1, 1, 1, 1, 1, 1, 1]
domein = [-1, 1, -1, 1]
z = [0]
naam = 'opdracht 3'
titel = 'plot van V op xy-vlak met kubus van deeltjes'
maakplot(deeltjesx, deeltjesy, deeltjesz, deeltjesq, domein, z, naam, titel)
print('opdracht 3 klaar')

############## opdracht 4 ##############
# om nu meerdere plaatjes op z = [0,0.25,0.5,0.75,1] te maken gebruik ik weer de functie, de kubus laat ik gelijk dus die variablen blijven staan
z = [0, 0.25, 0.5, 0.75, 1]
naam = 'opdracht 4'
titel = 'plots van V op diverse z \n met kubus van deeltjes'
# hier maak ik de contourplots duidelijk dat elke subplot dezelfde hoogtelijnen heeft
contourlines = [5, 5.25, 5.5, 5.75, 6, 6.25, 6.5, 6.75, 7,
                7.25, 7.5, 7.75, 8, 8.25, 8.5, 8.75, 9, 9.25, 9.5, 9.75, 10]
# om de z-waarde van onder naar boven te laten groeien draai ik de lijst om met [::-1]
maakplot(deeltjesx, deeltjesy, deeltjesz, deeltjesq,
         domein, z[::-1], naam, titel, nrows=len(z), contourhoogtes=contourlines)
print('opdracht 4 klaar')
