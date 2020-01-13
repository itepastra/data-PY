import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def hu(
    h0, hm, hk, d, alpha
):  # deze functie rekent de hoogte van een punt uit en returnt deze
    # h0 is de hoogte van het punt met de meetlat
    # hu is de hoogte van het punt waar de kijker op staat
    # hm is de afgelezen hoogte op de meetlat
    # d is de hemelbreedte tussen de meetlat en de kijker
    # alpha is de hoek van de horizontaalstelling
    return h0 + hm - hk - d * np.tan(alpha)


measurements = 1000000
# hier genereer ik 1000000 setjes van de inputvariabelen als normaalverdelingen met de gegevens die in het dictaat staan
hd = np.random.normal(321.90, 0.01, size=measurements)
h0 = np.random.normal(2.000, 0.005, size=measurements)
hk = np.random.normal(1.500, 0.005, size=measurements)
A0 = np.random.normal(140, 1, size=measurements)
alpha = np.random.normal(
    0, 0.4 * np.pi / (60 * 180), size=measurements
)  # een boogseconde is 1/60 graad, en 1 graad is pi/180 radiaal, en de tan-functie wil het in radialen

hh = hu(
    hd, h0, hk, A0, alpha
)  # de hoogte voor alle 1000000 meetwaarden worden hier in een array gestopt


fig = plt.figure("fig1")

# we hebben gekozen voor het aantal bins gelijk aan het aantal verschillende cijfers op 2 getallen achter de komma
bins = len(set(np.rint(hh * 100)))
# plt.hist maakt een histogram van de meetwaarden zodat er visueel goed te zien is of de normaalverdeling klopt, density maakt er een genormaliseerde histogram van
plt.hist(hh, bins=bins, density=True)


mu = np.mean(hh)
std = np.std(hh)
legendatext = (
    r"$H$ = " + str(round(mu, 2)) + "m \n" + r"$\sigma_H$ = " + str(round(std, 2)) + "m"
)  # hier maken we de tekst die linksonderin de plot komt te staan, zodat we deze kunnen zien

# print(mu, std)
xmin, xmax = min(hh), max(hh)
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)  # deze functie uit de scipy.stats library maakt een
#  lijn in de vorm van een normaaldistributie met gemiddelde mu en standaardafwijking std
plt.plot(
    x, p, linewidth=2
)  # we plotten de normaaldistributie over de histogram om te kijken of deze goed past
plt.xlabel("$h_H$ (m)", fontsize="large")
plt.yticks([])
plt.xticks(rotation=30)
plt.text(
    x=0.15,
    y=0.15,
    s=legendatext,
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.7),
    transform=fig.transFigure,
)
plt.savefig("fig 1")
# plt.show()
