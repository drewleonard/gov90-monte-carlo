import pickle
import matplotlib.pylab as plt

cj_20_240 = pickle.load(open("cj_20_240.p", "rb"))

lists = sorted(cj_20_240.items())

x, y = zip(*lists)

fig = plt.figure()
plt.plot(x, y)
fig.suptitle('CJ-20s Attacking Andersen AFB, Baseline Parameters + 240 ALCMs', fontsize=12)
plt.xlabel('Leaked CJ-20 ALCMs', fontsize=12)
plt.ylabel('Aircraft Destroyed', fontsize=12)
plt.grid()
plt.show()