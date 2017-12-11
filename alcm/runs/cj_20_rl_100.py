import os
import csv
import numpy as np
from random import *
from math import *
import operator
import pickle

# BASELINE VALUES FOR CJ-20 AIR LAUNCHED CRUISE MISSILE ATTACK
# FROM H-6K BOMBER AIRCRAFT
#
# CIRCULAR ERROR PROBABLE (CEP): 12.5 M
#
# SUBMUNITION N: 166 BOMBLETS
# SUBMUNITION PAYLOAD: 3 LB EACH
#
# SUBMUNITION DISTRIBUTION: CIRCULAR
# FOOTPRINT DIAMETER: 150 M
#
# MISSILES SENT: 120, TO 205 PARKING SLOTS
#
# MONTE CARLO ITERATIONS: 200

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

# HELPER FUNCTIONS


def ft_to_m(feet):

    return feet / 3.2808


def lb_to_kg(lb):

    return lb / 2.2046226218


def lethal_radius_m(yield_kg):

    # yield in kg
    # radius in m

    m = ft_to_m(20)
    kg = lb_to_kg(1)

    lethal_radius = m * (yield_kg / kg)**(1. / 3.)
    return lethal_radius  # (m)


def area_of_circle_m(radius):

    return pi * (radius**2)

# RETURN THE COORDINATES OF A GIVEN POINT (RADIUS (m), THETA (degrees))
# RELATIVE TO THE ANOTHER POINT'S COORDINATES


def haversine_location(lat1, lon1, radius, theta):

    r_earth = 6372800

    dx = radius * cos(theta)
    dy = radius * sin(theta)

    lat2 = lat1 + (dy / r_earth) * (180 / 3.14)
    lon2 = lon1 + (dx / r_earth) * (180 / 3.14) / cos(lat1 * 3.14 / 180)

    return(lat2, lon2)

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

# NON-VARIABLE CJ-20 ALCM DATA

cj_20_bomblets_n = 166

cj_20_bomblets_payload_lb = 3
cj_20_bomblets_payload_kg = lb_to_kg(cj_20_bomblets_payload_lb)

cj_20_bomblets_lethal_r = lethal_radius_m(cj_20_bomblets_payload_kg)

cj_20_bomblets_lethal_area = area_of_circle_m(
    cj_20_bomblets_lethal_r) * cj_20_bomblets_n

# VARIABLE CJ-20 ALCM DATA

cj_20_cep_m = 12.5 # between 5 m and 20 m estimates
cj_20_sent = 120 # from 20 H-6K bomber aircraft

# cj_20_dist_radius_m_var = [150, 200, 300]

cj_20_dist_radius_m = 100  # m (distributed circularly)
cj_20_dist_area_n = area_of_circle_m(cj_20_dist_radius_m)

# min() PREVENTS SSPK FROM EXCEEDING ONE

cj_20_sspk = min((cj_20_bomblets_lethal_area / cj_20_dist_area_n), 1)

# MONTE CARLO SIMULATION

monte_carlo_iterations = 200 # temporarily low value to spare my computer

sigma = cj_20_cep_m / 0.675  # getting normal distribution from CEP
mu = 0

cj_20_leaker_iterations = {}

# FOR EACH NUMBER OF LEAKERS POSSIBLE ...

for cj_20_leaker_n in range(0, cj_20_sent):

    print(cj_20_leaker_n)

    cj_20_success = []  # list to record success value each iteration of simulation

    # RUN SIMULATION OF CJ-20 ALCMS TARGETING AIRCRAFT

    for monte_carlo_iteration in range(0, monte_carlo_iterations):

        shuffle(cj_20_targets)  # ! leaked missiles have "random" targets

        cj_20_n = 0  # current missile

        cj_20_hit_locations = []  # locations of all missile hits

        # ITERATE OVER EACH MISSILE OF LEAKED MISSILES
        # TO DETERMINE WHERE EACH MISSILE LANDS

        while cj_20_n < cj_20_leaker_n:

            # DETERMINE RANDOM LOCATION OF MISSILE FROM NORMAL
            # DISTRIBUTION
            cj_20_hit_radius = np.random.normal(mu, sigma, 1)[0]

            # DETERMINE ANGLE RANDOMLY
            cj_20_hit_angle = randint(1, 360)

            # DETERMINE WHICH TARGET THE MISSILE IS SENT TO
            current_target = cj_20_n % len(cj_20_targets)

            # DETERMINE COORDINATES OF TARGET THE MISSILE IS SENT TO
            current_target_lat = cj_20_targets[current_target][0]
            current_target_lon = cj_20_targets[current_target][1]

            # DETERMINE MISSILE'S GEOGRAPHIC COORDINATES
            cj_20_hit_location = haversine_location(
                current_target_lat,
                current_target_lon,
                cj_20_hit_radius,
                cj_20_hit_angle)

            # RECORD MISSILE'S GEOGRAPHIC COORDINATES
            cj_20_hit_locations.append(cj_20_hit_location)

            # MOVE ON TO NEXT MISSILE
            cj_20_n += 1

        cj_20_targets_hits = {}

        # ITERATE OVER CJ-20 TARGETS

        for cj_20_target in cj_20_targets:

            # DETERMINE CJ-20 TARGET COORDINATES

            cj_20_target_loc_lat = cj_20_target[0]
            cj_20_target_loc_lon = cj_20_target[1]

            # ITERATE OVER CJ-20 HIT LOCATIONS

            for cj_20_hit_location in cj_20_hit_locations:

                # DETERMINE CJ-20 HIT LOCATION'S COORDINATES

                cj_20_hit_location_lat = cj_20_hit_location[0]
                cj_20_hit_location_lon = cj_20_hit_location[1]

                # DETERMINE CJ-20 HIT LOCATION'S DISTANCE FROM CURRENT CJ-20
                # TARGET

                cj_20_distance_from_cj_20_target = haversine_distance(cj_20_target_loc_lat,
                                                                      cj_20_target_loc_lon,
                                                                      cj_20_hit_location_lat,
                                                                      cj_20_hit_location_lon
                                                                      )

                # DETERMINE WHETHER MISSILE HIT SUFFICIENTLY CLOSE TO TARGET
                # SUCH THAT THE DISTANCE BETWEEN THE MISSILE AND TARGET IS LESS
                # THAN THE RADIUS OF THE MISSILE'S SUBMUNITION FOOTPRINT RADIUS

                if (cj_20_distance_from_cj_20_target < cj_20_dist_radius_m):

                    if cj_20_target[0] in cj_20_targets_hits:
                        cj_20_targets_hits[cj_20_target[0]] += 1

                    else:
                        cj_20_targets_hits[cj_20_target[0]] = 1

        cj_20_kills = 0

        # CALCULATIONS FOR TARGETS HIT BY CJ-20
        for key, value in cj_20_targets_hits.items():

            hits_n = value
            cj_20_target_pk = 1 - ((1 - cj_20_sspk)**hits_n)
            cj_20_kills += cj_20_target_pk

        cj_20_success.append(cj_20_kills)

    cj_20_expected_value = sum(cj_20_success) / float(len(cj_20_success))

    cj_20_leaker_iterations[cj_20_leaker_n] = cj_20_expected_value

print(cj_20_leaker_iterations)
# pickle.dump(cj_20_leaker_iterations, open("cj_20_rl_100.p", "wb"))