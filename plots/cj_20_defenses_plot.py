import pickle
import matplotlib.pylab as plt

cj_20_30_defenses = pickle.load( open( "cj_20_30_defenses.p", "rb" ) )
cj_20_60_defenses = pickle.load( open( "cj_20_60_defenses.p", "rb" ) )
cj_20_120_defenses = pickle.load( open( "cj_20_120_defenses.p", "rb" ) )
cj_20_240_defenses = pickle.load( open( "cj_20_240_defenses.p", "rb" ) )

cj_20_30_defenses_items = sorted(cj_20_30_defenses.items())
cj_20_60_defenses_items = sorted(cj_20_60_defenses.items())
cj_20_120_defenses_items = sorted(cj_20_120_defenses.items())
cj_20_240_defenses_items = sorted(cj_20_240_defenses.items())

m, n = zip(*cj_20_30_defenses_items)
q, r = zip(*cj_20_60_defenses_items)
s, t = zip(*cj_20_120_defenses_items)
x, y = zip(*cj_20_240_defenses_items)

fig = plt.figure()

plt.plot(m, n, "-r", label="30 CJ-20s")
plt.plot(q, r, "-b", label="60 CJ-20s")
plt.plot(s, t, "-g", label="120 CJ-20s")
plt.plot(x, y, "-m", label="240 CJ-20s")
plt.legend(loc='upper right')

fig.suptitle('USAF Defenses Against CJ-20 ALCMs', fontsize=14)
plt.xlabel('Effectiveness of USAF Defenses', fontsize=14)
plt.ylabel('Aircraft Destroyed', fontsize=14)
plt.grid()
plt.show()