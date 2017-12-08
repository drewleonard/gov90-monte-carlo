# CJ-20s WITH UNITARY WARHEADS
# CEP OF 5 m AND YIELD OF 400 kg

import os
import csv
import numpy as np
from random import *
from math import *
import pickle

# SUPPLY VALUES HERE

# CEP_LOW = 5  # (m)
# CEP_HIGH = 20  # (m)

# YIELD_LOW = 300  # (kg)
# YIELD_HIGH = 500  # (kg)

CEP = 5
YIELD = 400

CRUISE_MISSILES_SENT = 120

MONTE_CARLO_ITERATIONS = 400

# ! will increase lethal radius, as any part of aircraft within 
# warhead's lethal radius will destroy aircraft totally
AIRCRAFT_WINGSPAN = 14  # (m)


# READ IN GPS COORDINATES TO TARGET

cj_20_targets = []

parking_spots = os.path.expanduser(
    '/Users/drewnleonard/Documents/gov90-monte-carlo/data/205_parking_spots.csv')

with open(parking_spots) as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:

        split = row[0].split(",")
        lat = float(split[0])
        lon = float(split[1])
        cj_20_targets.append([lat, lon])

# HAVERSINE FORMULAS

# CALCULATE THE DISTANCE (m) BETWEEN TWO COORDINATES


def haversine_distance(lat1, lon1, lat2, lon2):

    R = 6372.8 * 1000  # earth radius in meters

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2)**2 + cos(lat1) * cos(lat2) * sin(dLon / 2)**2
    c = 2 * asin(sqrt(a))

    return R * c

# RETURN THE COORDINATES OF A GIVEN POINT (RADIUS (m), THETA (degrees))
# RELATIVE TO THE ANOTHER POINT'S COORDINATES


def haversine_location(lat1, lon1, radius, theta):

    r_earth = 6372800

    dx = radius * cos(theta)
    dy = radius * sin(theta)

    lat2 = lat1 + (dy / r_earth) * (180 / 3.14)
    lon2 = lon1 + (dx / r_earth) * (180 / 3.14) / cos(lat1 * 3.14 / 180)

    return(lat2, lon2)

# FUNCTION TO RETURN LETHAL RADIUS OF GIVEN YIELD
# TO AIRCRAFT THAT CAN SUSTAIN UP TO 20 KP OF OVERPRESSURE


def get_lethal_radius(current_yield):

    lethal_radius = 30 * (current_yield / 454)**(1. / 3.)
    return lethal_radius

# USE CUBE RULE TO CALCULATE LETHAL RADIUS (M)
# FOR 20 KILOPASCALS OF OVERPRESSURE FOR UNSHELTERED AIRCRAFT
# WHERE LETHAL RADIUS OF 454 KG FOR 20 KP OF OVERPRESSURE IS 30 M
# VALUES TAKEN FROM THE FOLLOWING SOURCE:
# http://www.inesap.org/sites/default/files/inesap_old/bulletin17/bul17art17.htm

lethal_radius = get_lethal_radius(YIELD)

# RECORD VALUES TO DRAW FROM NORMAL DISTRIBUTION

SIGMA = CEP / 0.675  # explain this (aka have Jack explain this)
MU = 0

# DICTIONARY TO STORE RESULTS FOR CURRENT COMBINATION OF CEP AND YIELD

n_leaked_missiles_results = {}

# FOR EACH NUMBER OF LEAKERS POSSIBLE ...

for n_leaked_missiles in range(0, CRUISE_MISSILES_SENT):

    print(n_leaked_missiles)

    success = []  # list to record success value each iteration of simulation

    # RUN SIMULATION OF MISSILES TARGETING AIRCRAFT

    for monte_carlo_iteration in range(0, MONTE_CARLO_ITERATIONS):

        n_missile = 0  # current missile

        missile_hit_locations = []  # locations of all missile hits

        # ITERATE OVER EACH MISSILE OF LEAKED MISSILES
        # TO DETERMINE WHERE EACH MISSILE LANDS

        while n_missile < n_leaked_missiles:

            # DETERMINE RANDOM LOCATION OF MISSILE FROM NORMAL
            # DISTRIBUTION
            missile_hit_radius = np.random.normal(MU, SIGMA, 1)[0]

            # DETERMINE ANGLE RANDOMLY
            missile_hit_angle = randint(1, 360)

            # DETERMINE WHICH TARGET THE MISSILE IS SENT TO
            current_target = n_missile % len(cj_20_targets)

            # DETERMINE COORDINATES OF TARGET THE MISSILE IS SENT TO
            current_target_lat = float(cj_20_targets[current_target][0])
            current_target_lon = float(cj_20_targets[current_target][1])

            # DETERMINE MISSILE'S GEOGRAPHIC COORDINATES
            missile_hit_location = haversine_location(
                current_target_lat,
                current_target_lon,
                missile_hit_radius,
                missile_hit_angle)

            # RECORD MISSILE'S GEOGRAPHIC COORDINATES
            missile_hit_locations.append(missile_hit_location)

            # MOVE ON TO NEXT MISSILE
            n_missile += 1

        hits = []  # list to record successfully targeted aircraft

        # ITERATE OVER TARGETS TO DETERMINE WHETHER THEY HAVE BEEN HIT
        # BY ANY MISSILES

        for target_loc in cj_20_targets:

            # DETERMINE TARGET COORDINATES

            target_loc_lat = float(target_loc[0])
            target_loc_lon = float(target_loc[1])

            # ITERATE OVER MISSILE HIT LOCATIONS

            for missile_hit_location in missile_hit_locations:

                # DETERMINE MISSILE'S COORDINATES

                missile_hit_location_lat = missile_hit_location[0]
                missile_hit_location_lon = missile_hit_location[1]

                # DETERMINE MISSILE'S DISTANCE FROM CURRENT TARGET

                distance_from_target = haversine_distance(target_loc_lat,
                                                          target_loc_lon,
                                                          missile_hit_location_lat,
                                                          missile_hit_location_lon
                                                          )

                # DETERMINE WHETHER MISSILE'S DISTANCE FROM TARGET
                # IS LESS THAN THE TARGET'S LETHAL RADIUS
                
                if distance_from_target < lethal_radius + AIRCRAFT_WINGSPAN:
                    hits.append(missile_hit_location)
                    break

        # RECORD NUMBER OF HITS DURING ITERATION OF SIMULATION

        success.append(len(hits))

    # CALCULATE AVERAGE OF THE ITERATION'S SUCCESS VALUES
    average = sum(success) / float(len(success))

    # RECORD AVERAGE SUCCESS FOR GIVEN NUMBER OF LEAKED CRUISE MISSILES
    n_leaked_missiles_results[n_leaked_missiles] = average

print(n_leaked_missiles_results)
pickle.dump(n_leaked_missiles_results, open("cj_20_unitary_baseline.p", "wb"))