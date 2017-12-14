import pickle
import matplotlib.pylab as plt

cj_20_baseline = pickle.load(open("cj_20_baseline.p", "rb"))

lists = sorted(cj_20_baseline.items())

x, y = zip(*lists)

fig = plt.figure()
plt.plot(x, y)
fig.suptitle('CJ-20s Striking Andersen AFB, Baseline Parameters', fontsize=14)
plt.xlabel('Leaked CJ-20 ALCMs', fontsize=14)
plt.ylabel('Aircraft Destroyed', fontsize=14)
plt.grid()
plt.show()