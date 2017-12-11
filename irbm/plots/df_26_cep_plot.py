# COMPARISON OF CJ-20s WITH VARYING CEP VALUES

import pickle
import matplotlib.pylab as plt

df_26_cep_50 = pickle.load(open("df_26_baseline.p", "rb"))
df_26_cep_150 = pickle.load(open( "df_26_cep_150.p", "rb" ))
df_26_cep_300 = pickle.load(open( "df_26_cep_300.p", "rb" ))

df_26_cep_50_list = sorted(df_26_cep_50.items())
df_26_cep_150_list = sorted(df_26_cep_150.items())
df_26_cep_300_list = sorted(df_26_cep_300.items())

q, r = zip(*df_26_cep_50_list)
x, y = zip(*df_26_cep_150_list)
s, t = zip(*df_26_cep_300_list)

fig = plt.figure()

plt.plot(q, r, '-r', label='DF-26, 50.0 m CEP')
plt.plot(x, y, '-b', label='DF-26, 150.0 m CEP')
plt.plot(s, t, '-g', label='DF-26, 300.0 m CEP')

plt.legend(loc='upper left')
fig.suptitle('DF-26s Attacking Andersen AFB, Varying CEP Values', fontsize=14)
plt.xlabel('Leaked DF-26 ALCMs', fontsize=14)
plt.ylabel('Aircraft Destroyed', fontsize=14)
plt.grid()
plt.show()