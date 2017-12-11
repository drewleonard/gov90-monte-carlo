import pickle
import numpy as np
import numpy.random
import matplotlib.pyplot as plt

df_26_hit_locations = pickle.load( open( "df_26_hex.p", "rb" ) )

x = [x[0] for x in df_26_hit_locations]
y = [x[1] for x in df_26_hit_locations]

# Make the plot
fig = plt.figure()
plt.hexbin(x, y, gridsize=(50,25),cmap=plt.cm.BuGn_r)
plt.colorbar()
fig.suptitle('10,000 Iterations of 50 DF-26 IRBMs', fontsize=14)
plt.xlabel('Latitude', fontsize=14)
plt.ylabel('Longitude', fontsize=14)
plt.show()