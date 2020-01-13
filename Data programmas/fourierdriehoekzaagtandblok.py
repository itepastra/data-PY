# dit programma doet hetzelfde als main.py, alleen maakt deze er ook een blokgolf bij

import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator
import numpy as np


# deze functie berekent de uitkomst van een bepaalde term uit de fourierserie
def fourierterm(A, i, t, f0, t0=0, fase=0):
    return A * np.sin(i * 2 * np.pi * f0 * (t - t0) + fase)


# deze functie telt de sinussen van alle losse termen bij elkaar op
def fourierreeks(Aj, t, f0):
    return sum([fourierterm(A, j, t, f0) for j, A in enumerate(Aj)])


# deze functie geeft de n-de term of de lijst tot de n-de term van de fourierreeks van de driehoeksgolf
def Dn(n, list=True):
    if list:
        Dns = []
        for i in range(n + 1):
            if i % 2 == 0:
                Dns.append(0)
            else:
                Dns.append(8 / (np.pi ** 2) * (((-1) ** ((i - 1) / 2)) / i ** 2))
        return Dns
    else:
        if n % 2 == 0:
            return 0
        else:
            return 8 / (np.pi ** 2) * (((-1) ** ((n - 1) / 2)) / n ** 2)


# deze functie kan de n-de term of een lijst tot en met de n-de term van de fourierreeks van de zaagtand teruggeven
def Zn(n, list=True):
    if list:
        Zns = [0]
        for i in range(1, n + 1):
            Zns.append(-1 / (i * np.pi))
        return Zns
    else:
        if n == 0:
            return 0
        else:
            return -1 / (n * np.pi)


# deze functie geeft een lijst of waarde tot/van de n-de term van de fourierreeks voor een blokgolf
def Sn(n, list=True):
    if list:
        Sns = []
        for i in range(n + 1):
            if i % 2 == 0:
                Sns.append(0)
            else:
                Sns.append(4 / (np.pi * i))
        return Sns
    else:
        if n % 2 == 0:
            return 0
        else:
            return 4 / (np.pi * n)


t = sp.Symbol("t")
f0 = sp.Symbol("f0")

# dit zijn de formules voor de driehoeksgolf, zaagtandgolf, blokgolf (square wave) en een sinus
D = 4 * sp.Abs(f0 * t + 1 / 4 - sp.floor(f0 * t + 3 / 4)) - 1
Z = f0 * t - sp.floor(f0 * t) - 1 / 2
S = 2 * (2 * sp.floor(f0 * t) - sp.floor(2 * f0 * t)) + 1
Sin = sp.sin(2 * sp.pi * f0 * t)

Dt = sp.lambdify([t, f0], D, "numpy")
Zt = sp.lambdify([t, f0], Z, "numpy")
St = sp.lambdify([t, f0], S, "numpy")
Sint = sp.lambdify([t, f0], Sin, "numpy")
print("setup klaar")


fig1 = plt.figure("figuur 1", dpi=500)

twaarden = np.linspace(0, 2, 10000)
f0waarde = 2

line1, = plt.plot(twaarden, Dt(twaarden, f0waarde))
line2, = plt.plot(twaarden, Zt(twaarden, f0waarde))
line3, = plt.plot(twaarden, St(twaarden, f0waarde))
line4, = plt.plot(twaarden, Sint(twaarden, f0waarde))

plt.legend([line1, line2, line3, line4], ["driehoek", "zaagtand", "blok", "sinus"])
# het zijn allemaal eenheidsloze functies, dus er is geen grootheid of eenheid voor de y-as
plt.ylabel("")
plt.xlabel("$t$")

plt.xlim(0, 2)

plt.savefig("PY6E-1")
print("1 klaar")
plt.close("all")
# na het opslaan sluiten we de figuur af zodat deze niet onnodig in het werkgeheugen blijft


fig2, axes2 = plt.subplots(3, 1, True, dpi=500, num="figuur 2", figsize=(6.4, 7.2))
f0waarde = 1  # we namen dit voor het gemak aan
# dit zijn een aantal willekeurig gekozen getallen die redelijk het verschil duidelijk maken
aantaltermen = [1, 2, 10, 50, 100, 1000]
# we stellen hier de kleuren van de lijnen in
colors = ["black", "blue", "red", "green", "maroon", "pink", "fuchsia", "purple"]
# een alpha van minder dan 1 maakt dat de lijn een beetje doorzichtig wordt, dit maakt de plot mooier
alpha = 0.6
# omdat er best veel lijnen in de plot staan maken we ze dunner (standaard is 2)
thickness = 1


for n, color in zip(aantaltermen, colors):
    axes2[0].plot(
        twaarden,
        fourierreeks(Dn(n), twaarden, f0waarde),
        color=color,
        alpha=alpha,
        lw=thickness,
    )
    axes2[1].plot(
        twaarden,
        fourierreeks(Zn(n), twaarden, f0waarde),
        color=color,
        alpha=alpha,
        lw=thickness,
    )
    axes2[2].plot(
        twaarden,
        fourierreeks(Sn(n), twaarden, f0waarde),
        color=color,
        alpha=alpha,
        lw=thickness,
    )

axes2[0].grid(which="both")
axes2[1].grid(which="both")
axes2[2].grid(which="both")
axes2[0].set_xlim(0, 2)
axes2[1].set_xlim(0, 2)
axes2[2].set_xlim(0, 2)

axes2[2].set_xlabel("$t$")

axes2[0].set_ylabel("")
axes2[1].set_ylabel("")
axes2[2].set_ylabel("")

plt.savefig("PY6E-2")
print("2 klaar")
plt.close("all")


fig3, axes3 = plt.subplots(3, 2, dpi=500, num="figuur 3", figsize=(6.4, 7.2))
# als inputs gebruiken we dezelfde waarden als in 2
# voor elk element in de lijst aantaltermen plotten we de kwadratische fout voor Z en D
# ook plotten we een ingezoomde versie aan de rechterkant zodat de verschillende pieken goed te zien zijn
for n, color in zip(aantaltermen, colors):
    Derror = (fourierreeks(Dn(n), twaarden, f0waarde) - Dt(twaarden, f0waarde)) ** 2
    Zerror = (fourierreeks(Zn(n), twaarden, f0waarde) - Zt(twaarden, f0waarde)) ** 2
    Serror = (fourierreeks(Sn(n), twaarden, f0waarde) - St(twaarden, f0waarde)) ** 2
    axes3[0][0].plot(twaarden, Derror, color=color, alpha=alpha, lw=thickness)
    axes3[1][0].plot(twaarden, Zerror, color=color, alpha=alpha, lw=thickness)
    axes3[0][1].plot(twaarden, Derror, color=color, alpha=alpha, lw=thickness)
    axes3[1][1].plot(twaarden, Zerror, color=color, alpha=alpha, lw=thickness)
    axes3[2][0].plot(twaarden, Serror, color=color, alpha=alpha, lw=thickness)
    axes3[2][1].plot(twaarden, Serror, color=color, alpha=alpha, lw=thickness)

axes3[0][0].set_xlim((0, 2))
axes3[1][0].set_xlim((0, 2))
axes3[2][0].set_xlim((0, 2))
# om de plots in te zoomen zetten we de xlim van de piek-0.15 tot de piek+0.15
axes3[0][1].set_xlim((1.1, 1.4))
axes3[1][1].set_xlim((0.85, 1.15))
axes3[2][1].set_xlim((0.85, 1.15))

# de ondergrens is 0, die zetten we hier
axes3[0][0].set_ylim(0)
axes3[0][1].set_ylim(0)
axes3[1][0].set_ylim(0)
axes3[1][1].set_ylim(0)
axes3[2][0].set_ylim(0)
axes3[2][1].set_ylim(0)

# hier maken we grids, deze maken het aflezen makkelijker
axes3[0][0].grid(which="both")
axes3[1][0].grid(which="both")
axes3[0][1].grid(which="both")
axes3[1][1].grid(which="both")
axes3[2][0].grid(which="both")
axes3[2][1].grid(which="both")

axes3[2][0].set_xlabel("$t$")
axes3[2][1].set_xlabel("$t$")

axes3[0][0].set_ylabel("lokale kwadratische fout")
axes3[1][0].set_ylabel("lokale kwadratische fout")
axes3[2][0].set_ylabel("lokale kwadratische fout")

plt.savefig("PY6E-3")
print("3 klaar")
plt.close("all")


fig4, ax = plt.subplots(num="figuur4", dpi=500)

f0waarde = 1  # we namen dit voor het gemak aan
maxiter = 2000
# dit is het grootste aantal iteraties van de fourierreeks die we berekenen
twaarden = np.linspace(
    0, 2, 2 * maxiter
)  # als het aantal waarden voor t 2 keer zo groot is als het aantal termen in de fourierserie blijkt de oppervlakte redelijk goed te kloppen
n = np.arange(maxiter)
Dfourier = np.zeros((maxiter, 2 * maxiter))
Zfourier = np.zeros((maxiter, 2 * maxiter))
Sfourier = np.zeros((maxiter, 2 * maxiter))
Derror = np.zeros(maxiter)
Zerror = np.zeros(maxiter)
Serror = np.zeros(maxiter)
# hier loopen we door de getallen tot maxiter in stapjes van stapgrootte en maken we lijstjes van de error in D en in Z
for i in n:
    # we printen hier de progress omdat het wel even duurt om uit te rekenen
    if i % int((maxiter / 100)) == 0:
        print(" progress: " + str(int(100 * i / maxiter)) + "%", end="\r")
    # we rekenen elke term steeds los uit omdat dat veel dubbel rekenwerk scheelt
    Dfourier[i, :] = fourierterm(Dn(i, False), i, twaarden, f0waarde)
    Zfourier[i, :] = fourierterm(Zn(i, False), i, twaarden, f0waarde)
    Sfourier[i, :] = fourierterm(Sn(i, False), i, twaarden, f0waarde)

    Derror[i] = np.mean((np.sum(Dfourier, axis=0) - Dt(twaarden, f0waarde)) ** 2)
    Zerror[i] = np.mean((np.sum(Zfourier, axis=0) - Zt(twaarden, f0waarde)) ** 2)
    Serror[i] = np.mean((np.sum(Sfourier, axis=0) - St(twaarden, f0waarde)) ** 2)


line1, = ax.plot(n, Derror, color="blue")
line2, = ax.plot(n, Zerror, color="red")
line3, = ax.plot(n, Serror, color="green")


ax.legend([line1, line2, line3], ["driehoeksgolf", "zaagtandgolf", "blokgolf"])

ax.set_xlim(0, maxiter)

plt.yscale("log")
# deze regel maakt dat we alle machten van 10 op de y-as krijgen
ax.yaxis.set_major_locator(LogLocator(base=10, subs=[1, 0], numdecs=4, numticks=15))
ax.grid(which="both", axis="both")

ax.set_xlabel("$N$")
ax.set_ylabel("gemiddeld kwadratisch verschil")

plt.savefig("PY6E-4")
print("4 klaar       ")
# plt.show()


# dit loopje gaat tot hele hoge termen uitrekenen wat de maximumwaarde is en deze printen in de console, gebruik ctrl-C, want het kan nogal lang duren
fouriertermen = []
for i in range(100000):
    twaarden = np.linspace(0.95, 1.05, i * 2)
    fouriertermen.append(Zn(i, False))
    if i % 100 == 1:
        print(
            " bij n = "
            + str(i)
            + " is de maximale waarde van de benadering "
            + str(np.amax(fourierreeks(fouriertermen, twaarden, f0waarde))),
            end="\r",
        )

