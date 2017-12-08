import pickle
import matplotlib.pylab as plt

cj_20_rl_100 = pickle.load(open("cj_20_rl_100.p", "rb"))
cj_20_rl_150 = pickle.load(open( "cj_20_baseline.p", "rb" ))
cj_20_rl_200 = pickle.load(open( "cj_20_rl_200.p", "rb" ))

cj_20_rl_100_list = sorted(cj_20_rl_100.items())
cj_20_rl_150_list = sorted(cj_20_rl_150.items())
cj_20_rl_200_list = sorted(cj_20_rl_200.items())

q, r = zip(*cj_20_rl_100_list)
x, y = zip(*cj_20_rl_150_list)
s, t = zip(*cj_20_rl_200_list)

fig = plt.figure()

plt.plot(q, r, '-r', label='CJ-20, Lethal Radius of 100 m')
plt.plot(q, r, '-b', label='CJ-20, Lethal Radius of 150 m')
plt.plot(q, r, '-g', label='CJ-20, Lethal Radius of 200 m')

plt.legend(loc='upper left')
fig.suptitle('CJ-20s Attacking Andersen AFB, Varying Lethal Radii', fontsize=14)
plt.xlabel('Leaked CJ-20 ALCMs', fontsize=14)
plt.ylabel('Aircraft Destroyed', fontsize=14)
plt.grid()
plt.show()