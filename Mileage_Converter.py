print("How many kilometres did you cycle today?")

#Taking user input
kms = input()

#Now to convert the user input to miles. Also using the round function to round to 3 decimal places.
miles = round(float(kms)*0.621371, 3)

#Final answer line.
print("Wow, that is amazing! You cycled " + str(miles) + " miles today.")