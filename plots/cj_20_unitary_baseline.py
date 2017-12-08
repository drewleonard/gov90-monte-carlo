import pickle
import matplotlib.pylab as plt

cj_20_unitary_baseline = pickle.load(open("cj_20_unitary_baseline.p", "rb"))
cj_20_sub_baseline = pickle.load( open( "cj_20_baseline.p", "rb" ) )

unitary = sorted(cj_20_unitary_baseline.items())
submunition = sorted(cj_20_sub_baseline.items())

x, y = zip(*unitary)
q, r = zip(*submunition)

fig = plt.figure()

# plt.plot(x, y, 'r--', q, r)
plt.plot(q, r, '-r', label='CJ-20, Submunition Warhead')
plt.plot(x, y, '-b', label='CJ-20, Unitary Warhead')
plt.legend(loc='upper left')
fig.suptitle('CJ-20s Attacking Andersen AFB, Unitary and Submunition', fontsize=14)
plt.xlabel('Leaked CJ-20 ALCMs', fontsize=14)
plt.ylabel('Aircraft Destroyed', fontsize=14)
plt.grid()
plt.show()