import numpy as np
import matplotlib.pyplot as plt

nbananen = 100000
Lstats = (15.5, 1.0)
dstats = (35.0, 5.0)
Rstats = (20.0, 3.0)
Astats = (2.2, 1.3)

n = np.array(np.arange(nbananen)).reshape(nbananen, 1)
d = np.array(np.random.normal(dstats[0], dstats[1], size=[nbananen, 1]))
L = np.array(np.random.normal(Lstats[0], Lstats[1], size=[nbananen, 1]))
R = np.array(np.random.normal(Rstats[0], Rstats[1], size=[nbananen, 1]))
A = np.array(np.random.normal(Astats[0], Astats[1], size=[nbananen, 1]))

neg = A < 0
A[neg] = 0

print(f'{nbananen} bananen gegenereerd')

dgoed = np.ma.masked_where(d < 27, d)
ndgoed = np.ma.masked_array.count(dgoed)
print(
    f'er zijn {ndgoed} goede bananen qua lengte van de {nbananen}, dit is ongeveer {np.rint(ndgoed/nbananen*100)}% \n')

Lgoed = np.ma.masked_where(L < 14, L)
banaanlosgoed = np.ma.concatenate((dgoed, Lgoed), axis=1)
banaangoed = np.ma.mask_rowcols(banaanlosgoed, 0)
nbanaangoed = np.ma.masked_array.count(banaangoed)/2

print(f'er zijn {int(nbanaangoed)} goede bananen qua lengte en dikte van de {nbananen}, dit is ongeveer {np.rint(nbanaangoed/nbananen*100)}% \n')


dmasked = np.ma.masked_where(d < 27, d)
Lmasked = np.ma.masked_where(L < 14, L)
Remask = np.array([not L[i]*1.25 < R[i] < L[i] *
                   1.3 for i in range(nbananen)]).reshape([nbananen, 1])
R1mask = np.array([not L[i]*1.2 < R[i] < L[i] *
                   1.4 for i in range(nbananen)]).reshape([nbananen, 1])
Re = np.ma.masked_array(R, Remask)
R1 = np.ma.masked_array(R, R1mask)
R2 = np.ma.masked_where(R < 0, R)
Ae = np.ma.masked_where(A > 1, A)
A1 = np.ma.masked_where(A > 2, A)
A2 = np.ma.masked_where(A > 4, A)

banaane = np.ma.concatenate((dmasked, Lmasked, Re, Ae), axis=1)
banaan1 = np.ma.concatenate((dmasked, Lmasked, R1, A1), axis=1)
banaan2 = np.ma.concatenate((dmasked, Lmasked, R2, A2), axis=1)
bem = np.ma.mask_rowcols(banaane, 0)
b1m = np.ma.mask_rowcols(banaan1, 0)
b2m = np.ma.mask_rowcols(banaan2, 0)

bemcount = np.ma.masked_array.count(bem)/4
b1mcount = np.ma.masked_array.count(b1m)/4 - bemcount
b2mcount = np.ma.masked_array.count(b2m)/4 - b1mcount - bemcount
brejectcount = np.ma.count_masked(b2m)/4

print(
    f'er zijn {bemcount} klasse extra bananen, dit is ongeveer {np.round(bemcount/nbananen*100,2)}%')
print(
    f'er zijn {b1mcount} klasse 1 bananen, dit is ongeveer {np.round(b1mcount/nbananen*100,2)}%')
print(
    f'er zijn {b2mcount} klasse 2 bananen, dit is ongeveer {np.round(b2mcount/nbananen*100,2)}%')
print(
    f'er zijn {brejectcount} geweigerde bananen, dit is ongeveer {np.round(brejectcount/nbananen*100,2)}%')
print(
    f'samen is dit {(bemcount + b1mcount + b2mcount + brejectcount)/nbananen*100}%')
