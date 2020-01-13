import numpy as np
import matplotlib.pyplot as plt

# met behulp van dit bestand is het mogelik om bij n deeltjes met elk een lading q en een coordinaat in R^3 een contourplot van de coulombpotentiaal te maken van een vlak op hoogte z
# hierbij maak ik gebruik van trucjes die we nog niet hebben gehad zodat het minder typwerk is


# deze functie neemt een verschil in x,y,z en berekent de coulombpotentiaal in dat punt
def V(deltax=0, deltay=0, deltaz=0, q=1, maxvalue=100):
    return np.ma.masked_greater(
        q / (np.sqrt(deltax ** 2 + deltay ** 2 + deltaz ** 2)), maxvalue
    )


def maakplot(
    deeltjes=np.array([]),
    domein=[-1, 1, -1, 1],
    z=[0],
    naam="maakplot",
    titel="titel",
    layers=15,
    nrows=1,
    ncols=1,
):
    x = np.linspace(domein[0], domein[1], 400)
    y = np.linspace(domein[2], domein[3], 400)
    X, Y = np.meshgrid(x, y)

    fig = plt.figure(naam, figsize=(5 * ncols, 4 * nrows))
    # ik zorg dat er een lege lijst is met een lang genoege lengte om alle subplots te gaan bevatten zodat mijn for loop goed werkt
    ax = [0 for i in range(nrows * ncols)]
    # print(ax)

    # hier tel ik de waarden van V voor elk punt voor elk deeltje op waardoor ik voor elk punt de coulombpotentiaal krijg in een 2D numpy array
    for p, j in enumerate(z):
        # hier reken ik per deeltje V uit op elk punt en neem hier de som vervolgens van
        v = sum(
            [
                V(
                    X - deeltjes[i][0],
                    Y - deeltjes[i][1],
                    j - deeltjes[i][2],
                    deeltjes[i][3],
                )
                for i in range(len(deeltjes))
            ]
        )

        ax[p] = fig.add_subplot(nrows, ncols, p + 1)
        # uncomment een van de 2 regels hieronder om te kiezen tussen contourplots of contourfplots
        cmap = ax[p].contourf(X, Y, v, levels=layers)
        # cmap = ax[p].contour(X, Y, v, levels=layers)
        ax[p].axis("scaled")
        ax[p].set_ylabel("z = " + str(j))
        fig.colorbar(cmap)

    plt.axis(domein)
    plt.suptitle(titel)
    plt.savefig(naam)


n = int(input("hoeveel deeltjes "))
deeltjes_string = [
    tuple(input("coordinaten deeltje " + str(i) + " in de vorm: x y z q ").split(" "))
    for i in range(n)
]
domein = input("wat is het domein in de vorm: xmin xmax ymin ymax ").split(" ")
z_waarden = input("lijst met z-waarden om te plotten in de vorm: z1 z2 ... zn").split(
    " "
)
naam = input("hoe moet het opgeslagen plaatje heten? ")
titel = input("wat is de titel van de plot? ")

# hier maak ik een array van mijn coordinaten en maak ik het floats i.p.v. strings
deeltjes_num = np.array(
    [tuple([float(item) for item in tup]) for tup in deeltjes_string]
)
# dit doe ik ook voor het domein en voor z
domein = [float(i) for i in domein]
z_waarden = [float(i) for i in z_waarden]

maakplot(deeltjes_num, domein, z_waarden, naam, titel, nrows=len(z_waarden))
