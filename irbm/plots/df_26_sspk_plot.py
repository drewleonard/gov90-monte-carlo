import pickle
import matplotlib.pylab as plt

df_26_sspk = pickle.load(open("df_26_sspk.p", "rb"))

df_26_sspk_list = sorted(df_26_sspk.items())

x, y = zip(*df_26_sspk_list)

fig = plt.figure()

plt.plot(x, y, '-r', label='')
fig.suptitle('DF-26s Attacking Andersen AFB, Probability of Kill', fontsize=14)
plt.xlabel('Number of DF-26 IRBMs Hitting an Aircraft', fontsize=14)
plt.ylabel('Probability of Kill', fontsize=14)
plt.grid()
plt.show()