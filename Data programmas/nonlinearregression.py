import sympy
import numpy as np
import matplotlib.pyplot as plt
import scipy.odr as odr


def A(d):
    return d ** 2


def B(l, T, p, L):
    return (2 * l * T) / (p * L)


def D(A: list, t: float):
    return np.sqrt(A[0] + A[1] * t)


t = np.linspace(0, 9, 1000)
tmeet = np.array([0.25, 0.75, 1.25, 2.5, 3.0, 3.75, 4.5, 5.5, 7.0, 8.5])
dmeet = np.array([1.43, 2.06, 2.09, 2.66, 3.31, 3.52, 3.79, 4.12, 4.35, 4.95])
sig_dmeet = np.array([0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20])

astart = 1
bstart = 2

odr_model = odr.Model(D)
odr_data = odr.RealData(tmeet, dmeet, sy=sig_dmeet)
odr_obj = odr.ODR(odr_data, odr_model, beta0=[astart, bstart])
odr_obj.set_job(fit_type=2)

odr_res = odr_obj.run()

par_best = odr_res.beta
par_sig = odr_res.sd_beta
par_cov = odr_res.cov_beta
odr_res.pprint()

fig, ax = plt.subplots(num="figuur 1")

(line1,) = ax.plot(
    t, D(par_best, t), color="blue", zorder=5
)  # we plotten de beste schatter volgens scipy.odr

line2 = ax.fill_between(
    t,
    D(par_best - par_sig, t),  # hier vullen we de schatter min een sigma in
    D(par_best + par_sig, t),  # hier de schatter plus 1 sigma
    color="lightblue",
    zorder=0,  # zorder bepaalt welke grafiek bovenop komt, we willen het vlak
    alpha=0.8,
)

line3 = ax.errorbar(
    tmeet,  # de tijd van de meetwaarden
    dmeet,  # de beste schatters
    sig_dmeet,  # de bijbehorende onzekerheden
    marker="d",
    ls=" ",
    capsize=2,
    capthick=0.5,
    color="orange",
    zorder=10,
)  # we willen de metingen bovenaan

paramtext = (
    f"$A$ = {par_best[0].round(2)} "
    + r"$\pm$"
    + f" {par_sig[0].round(2)} cm$^2$"
    + f"\n$B$ = {par_best[1].round(2)} "
    + r"$\pm$"
    + f" {par_sig[1].round(2)} cm$^2$/uur"
)  # hier maken we de tekst voor het tekstvakje rechtsonderin
plt.text(
    x=0.6,
    y=0.15,
    s=paramtext,
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.7),
    transform=fig.transFigure,
)  # dit tekstvak laat de beste schatters voor A en B zien, met bijbehorende onzekerheden

ax.legend(
    (line3, line1, line2), ("meetpunten", "beste model", "onzekerheid model")
)  # de legenda voor de grafieken
ax.set_xlabel("$t$ (uren)")
ax.set_ylabel("$d$ (cm)")
ax.set_xlim(0, 9)
ax.set_ylim(1, 5.5)
ax.grid()

plt.savefig("fig 1", dpi=400)
