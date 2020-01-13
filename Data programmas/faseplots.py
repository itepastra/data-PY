import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.widgets import Slider
from matplotlib import ticker


def filepath(filename):  # deze functie geeft het path van het bestand zelf terug hoe je het ook uitvoert, zodat het programma het bestand goed kan vinden
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)


def update(val):
    n = int(sn.val)
    l1.set_ydata(amplitude1[n]*np.sin(t*hoekfrequencies[n]+phase1[n]))
    l2.set_ydata(amplitude2[n]*np.sin(t*hoekfrequencies[n]+phase2[n]))
    text1.set_text(legendatext(n))


def legendatext(n):
    return '\n'.join(['meetwaarden', '$f$ = '+str(frequencies[n])+' Hz', r'$f$ = '+str(int(hoekfrequencies[n]))+r' $\omega$', '$gain$ = '+str(gain[n]), r'$\Delta\phi$ = '+str(phasedif[n])+r' $\omega$'])


filename = 'bewerkte_data.txt'


datamatrix = np.genfromtxt(filepath(filename))
datamatrix_T = datamatrix.transpose()

frequencies = datamatrix_T[0]
# de sinussen moeten met de hoekfrequentie worden berekend
hoekfrequencies = frequencies * 2 * np.pi
amplitude1 = datamatrix_T[1]
phase1 = datamatrix_T[2]
amplitude2 = datamatrix_T[3]
phase2 = datamatrix_T[4]
gain = datamatrix_T[5]
phasedif = datamatrix_T[6]
nstart = 25
t = np.linspace(0, 10/hoekfrequencies[nstart], 1000)


fig, ax = plt.subplots(1, 1, num='figuur 1',
                       sharex=True, sharey=False, figsize=(10, 8))
plt.subplots_adjust(bottom=0.15)

l1, = ax.plot(t, amplitude1[nstart] *
              np.sin(hoekfrequencies[nstart]*t+phase1[nstart]))
l2, = ax.plot(t, amplitude2[nstart] *
              np.sin(hoekfrequencies[nstart]*t+phase2[nstart]))
ax.set_ylim(-np.ceil(max(amplitude1+amplitude2)/2),
            np.ceil(max(amplitude1+amplitude2)/2))
ax.set_xlim(0, max(t))
# hier maak ik dat de x as de tijd in ms laat zien
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: 1000 * x))
ax.set_xlabel('$t$ (ms)')
ax.set_ylabel('$v$ (V)')
text1 = ax.text(x=0.05, y=0.05, s=legendatext(nstart), transform=ax.transAxes,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
ax.legend([l1, l2], ['$v_i$ (t)', '$v_u$ (t)'], loc='upper right')

axn = plt.axes([0.20, 0.04, 0.65, 0.03])

sn = Slider(axn, 'meting', 0, len(frequencies)-1, valinit=nstart, valstep=1)
sn.on_changed(update)


plt.show()
