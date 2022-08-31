# Brian Diosan

# establish list the space probes
spaceProbes = ["Pioneer 10", "Pioneer 11", "Voyager 1", "Voyager 2", "New Horizons"]

# get the total number of probes
totalProbes = len(spaceProbes)

# establish the list of distances to the probes
distanceToProbes = [123, 100, 145, 123, 43]

#  establish conversion factors
AU_TO_METERS = 149597870700
AU_TO_MILES = 93000000


# loop through each probe to print out the distances
for probeNumber in range(totalProbes) :
    currentProbe = spaceProbes[probeNumber]
    currentDistance = distanceToProbes[probeNumber]

    # calculate the distances
    distanceInMeters = currentDistance * AU_TO_METERS
    distanceInMiles = currentDistance * AU_TO_MILES

    # print the probe and the distance
    print(currentProbe + " Distance in km " + str(distanceInMeters / 1000) + ", Distance in mi " + str(distanceInMiles))
