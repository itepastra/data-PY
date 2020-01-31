import numpy as np
import matplotlib.pyplot as plt
import os


def filepath(
    filename,
):  # deze functie geeft het path van het bestand zelf terug hoe je het ook uitvoert, zodat het programma het bestand goed kan vinden
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)


def runningMean(values, n=0):
    values = np.array(values)
    if n <= 0 or n >= len(values):
        # als n niet gegeven is of niet in de goeie range dan geeft de functie gewoon het volledige gemiddelde
        return [np.mean(values)]
    elif len(values.shape) > 1:
        v = None
        for i in range(values.shape[1]):
            vals = values[:, i]
            rvals = np.array([runningMean(vals, n)]).T
            if v is not None:
                v = np.concatenate([v, rvals], axis=1)
            else:
                v = rvals

        # als er een matrix in wordt gedaan zal de functie de rijen middelen i.p.v. de kolommen
        return v
    else:
        # deze list comprehension maakt een lijst met de lopende gemiddelden met lengte n,
        # en gaat van het begin tot het einde
        return [np.mean(values[a : n + a]) for a in range(len(values) - n + 1)]


def exponential(exp, t, pos=0):  # deze functie geeft de exponentiele groei voor vraag g
    if pos == 0:
        return concentratie[0] * exp ** t
    else:
        a = exp ** t[pos]
        b = 411.439 / a
        # b is de juiste startwaarde want a is de verhouding beginwaarde tot eindwaarde
        return b * exp ** t


# importeer de data van het bestand
data = np.genfromtxt(filepath("co2_mm_mlo.txt"))

# print het aantal rijen en kolommen
print(
    f"de lengte van de rijen = {np.size(data, 0)} en er zijn {np.size(data,1)} kolommen"
)

# we pakken de 3e en 5e kolom van de matrix
tijd = data[:, 2]
concentratie = data[:, 4]

# we pakken de running average van de tijd en de concentratie over 12 maanden
runningconcentration = runningMean(concentratie, 12)
runningtime = runningMean(tijd, 12)

fig, ax = plt.subplots(1, 1)
l1 = ax.scatter(tijd, concentratie, marker="d", s=2)
(l2,) = ax.plot(runningtime, runningconcentration, color="red")
ax.set_xlim(tijd[0], tijd[-1])
ax.set_xlabel("tijd (jaar)")
ax.set_ylabel("CO$_2$ concentratie (ppm)")

plt.legend(
    (l1, l2), ["gemeten concentratie CO$_2$", "lopend gemiddelde van 12 maanden"]
)

plt.grid(True)
plt.savefig("CO2_lopend_gemiddelde", dpi=400)

# g

fig, ax = plt.subplots()
t = np.linspace(
    tijd[0], tijd[-1], 1000
)  # we laten t lopen tussen het begin en einde van de tijdsinterval
tred = (
    t - t[0]
)  # tred begint bij 0, dit is nodig om de exponentiele groei makkelijker te maken en deze heeft dezelfde lengte als t


(l1,) = ax.plot(t, exponential(1.0024, tred), zorder=0)
(l2,) = ax.plot(t, exponential(1.006, tred, -1), zorder=5)
(l3,) = ax.plot(runningtime, runningconcentration, zorder=10, lw=2)
l4 = ax.scatter(
    runningtime[10::12], runningconcentration[10::12], marker="d", s=16, zorder=15
)

ax.set_xlim(tijd[0], tijd[-1])
ax.set_xlabel("tijd (jaar)")
ax.set_ylabel("CO$_2$ concentratie (ppm)")

plt.legend(
    (l1, l2, l3, l4),
    [
        "exponentiele groei 0,24% per jaar",
        "exponentiele groei 0,6% per jaar",
        "lopend gemiddelde van 12 maanden",
        "gemeten concentratie CO$_2$",
    ],
)

plt.grid(True)
plt.savefig("exponentiele_trends", dpi=400)

# h
# we kunnen concluderen dat de CO2 concentratie toeneemt in de tijd,
# omdat de lijn exponentiele groei volgt is de toename in de CO2 concentratie ook aan het toenemen
# de 2e afgeleide van een exponentiele groeifunctie is ook positief dus de snelheid van de toename neemt ook toe


# de functie runningmean werkt met arrays, dit heb ik echter nergens hoeven gebruiken
# print(runningMean([[1, 2], [2, 3], [3, 4]], 2))

