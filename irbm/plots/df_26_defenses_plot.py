import pickle
import matplotlib.pylab as plt

df_26_12_defenses = pickle.load( open( "df_26_12_defenses.p", "rb" ) )
df_26_25_defenses = pickle.load( open( "df_26_25_defenses.p", "rb" ) )
df_26_50_defenses = pickle.load( open( "df_26_50_defenses.p", "rb" ) )
df_26_100_defenses = pickle.load( open( "df_26_100_defenses.p", "rb" ) )

df_26_12_defenses_items = sorted(df_26_12_defenses.items())
df_26_25_defenses_items = sorted(df_26_25_defenses.items())
df_26_50_defenses_items = sorted(df_26_50_defenses.items())
df_26_100_defenses_items = sorted(df_26_100_defenses.items())

m, n = zip(*df_26_12_defenses_items)
q, r = zip(*df_26_25_defenses_items)
s, t = zip(*df_26_50_defenses_items)
x, y = zip(*df_26_100_defenses_items)

fig = plt.figure()

plt.plot(m, n, "-r", label="12 DF-26s")
plt.plot(q, r, "-b", label="25 DF-26s")
plt.plot(s, t, "-g", label="50 DF-26s")
plt.plot(x, y, "-m", label="100 DF-26s")
plt.legend(loc='upper right')

fig.suptitle('USAF Defenses Against DF-26 IRBMs', fontsize=14)
plt.xlabel('Percent of IRBMs Intercepted', fontsize=14)
plt.ylabel('Aircraft Destroyed', fontsize=14)
plt.grid()
plt.show()