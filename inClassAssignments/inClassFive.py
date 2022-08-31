
# Brian Diosan

#Sine Without Factorial

x_radian = float(input("Enter Angle in Radian: "))

N = int(input("Number of Terms In Sine Series"))


# initialize sine
sine = 0

# initialize sign
sign = 1

# initialize factorial
factorial = 1

for n in range(1, 2*N-1):
    if n % 2 != 0 :
        sine += (sign * x_radian**n)/factorial
        sign *= -1
    factorial *= (n+1)

print(sine)