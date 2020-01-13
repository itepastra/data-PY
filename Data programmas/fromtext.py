import numpy as np
import matplotlib.pyplot as plt
import os


def filepath(
    filename
):  # deze functie geeft het path van het bestand zelf terug hoe je het ook uitvoert, zodat het programma het bestand goed kan vinden
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)


filename = "bewerkte_data.txt"
data_in = open(filepath(filename), "r")


# ================= opdracht 2 =================#

# hier importeer ik de datamatrix en de losse tekst als datamatrix en filedata
datamatrix = np.genfromtxt(filepath(filename))
filedata = data_in.readlines()

paramiterator = -1
params = []
paramtypes = []

for line in filedata:
    if "#  *PARA" in line:  # de line #   *PARA komt maar 1 keer voor in het bestand
        # na de line heb ik het aantal parameters gezet voor het inlezen
        paramiterator = int(line[-2])
    elif paramiterator > 0:
        # hier lees ik de waarde van de parameter af
        params.append(float(line.split("\t")[-1][:-1]))
        # hier lees ik het type parameter af
        paramtypes.append(line.split("\t")[-2])
        paramiterator -= 1
    elif (
        paramiterator == 0
    ):  # na de parameters komen de headers van de tabel, die lees ik hier in en die print ik
        head = "   " + " ".join(
            [argument.ljust(15) for argument in line[3:].split("\t")]
        )
        print(head)
        paramiterator -= 1

# np.set_printoptions kan mij laten instellen hoe de getallen worden geprint op het scherm, in dit geval aan de linkerkant van 15 karakter lange blokken
np.set_printoptions(
    formatter={
        "all": lambda x: str(" " + str(round(x, 3))).replace(" -", "-").ljust(15)
    },
    linewidth=150,
)
print(datamatrix)

# onderaan print ik alle parameters met de eenheid (paramtype) en welke parameter het is
for i, paramtype, param in zip(range(1, len(params) + 1), paramtypes, params):
    print(f"Parameter {i} = {param} {paramtype}")


# ================= opdracht 3 =================#


datamatrix_T = datamatrix.transpose()

frequencies = datamatrix_T[0]
amplitude1 = datamatrix_T[1]
phase1 = datamatrix_T[2]
amplitude2 = datamatrix_T[3]
phase2 = datamatrix_T[4]
gain = datamatrix_T[5]
phasedif = datamatrix_T[6]
nstart = 25
t = np.linspace(0, 10 / frequencies[nstart], 1000)

fig, axes = plt.subplots(
    2, 1, num="figuur 1", sharex=True, sharey=False, figsize=(6, 8)
)

legendatext = "\n".join(
    ["parameters"]
    + [
        str(param) + " " + str(paramtype)
        for param, paramtype in zip(params, paramtypes)
    ]
)

axes[0].plot(frequencies, gain, color="#AEA04B")
axes[0].set_xscale("log")
axes[0].set_xlabel("$f$ (Hz)")
axes[0].set_ylabel("$A_2/A_1$")
axes[0].grid(True, "both")

axes[1].plot(frequencies, phasedif, color="#5F021F")
axes[1].set_xscale("log")
axes[1].set_xlabel("$f$ (Hz)")
axes[1].set_ylabel(r"$\Delta\phi$ ($\omega$)")
axes[1].grid(True, "both")
axes[1].text(
    x=0.05,
    y=0.05,
    s=legendatext,
    transform=axes[1].transAxes,
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.7),
)


plt.savefig("plot.pdf")
# plt.show()
