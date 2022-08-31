# Brian Diosan

# establish list the space probes
import math


spaceProbes = ["Pioneer 10", "Pioneer 11", "Voyager 1", "Voyager 2", "New Horizons"]

# get the total number of probes
totalProbes = len(spaceProbes)

# establish the list of distances to the probes
distanceToProbes = [123, 100, 145, 123, 43]

distanceToProbesInMeters = []

#  establish conversion factors
AU_TO_METERS = 149597870700

# this is in meters per second
SPEED_OF_LIGHT = 299792458

timeInMin = []
timeInSec = []

# loop through each probe to print out the distances
for probeNumber in range(totalProbes) :
    currentProbe = spaceProbes[probeNumber]
    currentDistance = distanceToProbes[probeNumber]

    # calculate the distances in KM
    distanceInMeters = currentDistance * AU_TO_METERS
    distanceToProbesInMeters.append(distanceInMeters)

    # calculate the time it takes for radiowaves to get to probes in seconds
    timeInSeconds = distanceToProbesInMeters[probeNumber] / SPEED_OF_LIGHT

    # append the results to the list
    timeInSec.append(math.ceil(timeInSeconds))
    timeInMin.append(math.ceil(timeInSeconds / 60))


# print the results
print(spaceProbes)
print(timeInSec)
print(timeInMin)