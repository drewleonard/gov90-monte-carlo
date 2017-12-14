# COMPARISON OF CJ-20s WITH VARYING CEP VALUES

import pickle
import matplotlib.pylab as plt

cj_20_cep_12_5 = pickle.load(open("cj_20_baseline.p", "rb"))
cj_20_cep_20 = pickle.load(open( "cj_20_cep_20.p", "rb" ))
cj_20_cep_50 = pickle.load(open( "cj_20_cep_50.p", "rb" ))

cj_20_cep_12_5_list = sorted(cj_20_cep_12_5.items())
cj_20_cep_20_list = sorted(cj_20_cep_20.items())
cj_20_cep_50_list = sorted(cj_20_cep_50.items())

q, r = zip(*cj_20_cep_12_5_list)
x, y = zip(*cj_20_cep_20_list)
s, t = zip(*cj_20_cep_50_list)

fig = plt.figure()

plt.plot(q, r, '-r', label='CJ-20, 12.5 m CEP')
plt.plot(x, y, '-b', label='CJ-20, 20.0 m CEP')
plt.plot(s, t, '-g', label='CJ-20, 50.0 m CEP')

plt.legend(loc='upper left')
fig.suptitle('CJ-20s Striking Andersen AFB, Varying CEP Values', fontsize=14)
plt.xlabel('Leaked CJ-20 ALCMs', fontsize=14)
plt.ylabel('Aircraft Destroyed', fontsize=14)
plt.grid()
plt.show()