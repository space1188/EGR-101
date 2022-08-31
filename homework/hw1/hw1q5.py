# Brian Diosan

# Establish the constants
typeOfEmitter = ["Radio", "Microwave", "Infrared", "Visible", "Ultraviolet"]
frequencyInHz = [300000000.0, 10000000000.0, 300000000000.0, 600000000000000.0, 900000000000000.0]

# this is in meters per second
SPEED_OF_LIGHT = 299792458

# create list to put the results in
resultingWavelengths = []

# loop through each type of emitter to calculate each wavelength
for i in range(0, len(typeOfEmitter)) :
    # append the resulting wavelength to the list respectively
    resultingWavelengths.append(SPEED_OF_LIGHT / frequencyInHz[i])


# print the results
print(typeOfEmitter)
print(frequencyInHz)
print(resultingWavelengths)