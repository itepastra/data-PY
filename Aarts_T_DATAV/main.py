import numpy as np
import matplotlib.pyplot as plt
import os
import scipy.odr as odr
import scipy.optimize as op


def filepath(
    filename,
):  # deze functie geeft het path van het bestand zelf terug hoe je het ook uitvoert, zodat het programma het bestand goed kan vinden
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)


def f(B, theta):
    return B[0] * (np.sinc((B[2] / B[3]) * np.sin(theta))) ** 2 + B[1]


data = np.genfromtxt(filepath("DataV2020_input.txt"), delimiter=",")
theta = data[:, 0]
I = data[:, 1]
sigI = data[:, 2]

fig, ax = plt.subplots()
ax.errorbar(theta, I, yerr=sigI, ecolor="#00FF0060")
ax.set_xlabel("$\\Theta$ (Radialen)")
ax.set_ylabel("gemeten intensiteit")
ax.set_ylim(0)

plt.savefig("data gevisualiseerd", dpi=400)

Bstart = [1100, 100, 7.5e-6, 532e-9]
odr_model = odr.Model(f)

odr_data = odr.RealData(theta, I, sy=sigI)

odr_obj = odr.ODR(odr_data, odr_model, beta0=Bstart)

odr_obj.set_job(fit_type=2)
odr_res = odr_obj.run()
par_best = odr_res.beta
chi2red = odr_res.res_var
print(par_best, chi2red)
odr_res.pprint()
ax.plot(theta, f(par_best, theta), color="red", zorder=100)


plt.savefig("ODR")

fig2, ax2 = plt.subplots()
ax2.plot(theta, sigI ** 2)

ax2.set_xlabel("$\\Theta$ (Radialen)")
ax2.set_ylabel("$\sigma^2$")
ax2.set_ylim(0)
plt.savefig("variantietheta")
