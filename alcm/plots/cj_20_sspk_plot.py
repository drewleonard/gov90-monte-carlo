import pickle
import matplotlib.pylab as plt

cj_20_sspk = pickle.load(open("cj_20_sspk.p", "rb"))
# cj_20_sub_baseline = pickle.load( open( "cj_20_baseline.p", "rb" ) )

cj_20_sspk_list = sorted(cj_20_sspk.items())
# submunition = sorted(cj_20_sub_baseline.items())

x, y = zip(*cj_20_sspk_list)
# q, r = zip(*submunition)

fig = plt.figure()

# plt.plot(x, y, 'r--', q, r)
plt.plot(x, y, '-r', label='')
# plt.plot(x, y, '-b', label='CJ-20, Unitary Warhead')
# plt.legend(loc='upper left')
fig.suptitle('CJ-20s Attacking Andersen AFB, Probability of Kill', fontsize=14)
plt.xlabel('Number of CJ-20 ALCMs Hitting an Aircraft', fontsize=14)
plt.ylabel('Probability of Kill', fontsize=14)
plt.grid()
plt.show()