# Brian Diosan
# inClassTwo.py
# estimating speed for the three routes

# conversion factor
MIN2HR = 60

# set distance vars for the three routes (in miles)
r1Distance = 109
r2Distance = 120
r3Distance = 136

# set time vars for the three routes (in minutes)
r1Time = 60 + 44
r2Time = 120 + 3
r3Time = 120 + 23

# calculate speed vars for the three routes (to mph)
r1Speed = r1Distance / r1Time * MIN2HR
r2Speed = r2Distance / r2Time * MIN2HR
r3Speed = r3Distance / r3Time * MIN2HR

# print out the results
print("Route One Speed in MPH is " + str(r1Speed))
print("Route Two Speed in MPH is " + str(r2Speed))
print("Route Three Speed in MPH is " + str(r3Speed))
