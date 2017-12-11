import pickle
import numpy as np
import numpy.random
import matplotlib.pyplot as plt

cj_20_hit_locations = pickle.load( open( "cj_20_hex.p", "rb" ) )

x = [x[0] for x in cj_20_hit_locations]
y = [x[1] for x in cj_20_hit_locations]

# Make the plot
fig = plt.figure()
plt.hexbin(x, y, gridsize=(50,25),cmap=plt.cm.BuGn_r)
plt.colorbar()
fig.suptitle('10,000 Iterations of 120 CJ-20 ALCMs', fontsize=14)
plt.xlabel('Latitude', fontsize=14)
plt.ylabel('Longitude', fontsize=14)
plt.show()