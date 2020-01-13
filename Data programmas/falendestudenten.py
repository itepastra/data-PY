import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

nstudenten = int(input('hoeveel studenten? '))
nopgaven = int(input('hoeveel opgaven? '))
ntoetsen = int(input('hoeveel toetsen? /'))
naam = np.array([str(i) for i in range(nstudenten)])
stno = np.array(range(nstudenten))


def toets():
    opg = np.concatenate(
        [np.array(np.random.uniform(1, 10, size=[nstudenten, 1])) for i in range(nopgaven)], 1)

    vol_masker = [np.mean(student) > 6 for student in opg]

    # Nu kan selectie plaatsvinden
    vol_naam = naam[vol_masker]
    vol_stno = stno[vol_masker]
    vol_cijfer = opg[vol_masker]

    print("Studenten met een voldoende:")
    for it in np.arange(len(vol_naam)):
        print("%s (studnr %s ) heeft %s punten" %
              (vol_naam[it],   # afbreken van lange regels
               vol_stno[it],
               np.mean(vol_cijfer[it])))
    return vol_masker.count(True)


resultaten = []
for i in range(ntoetsen):
    resultaten.append(toets())

print(resultaten)
print(np.mean(resultaten))
