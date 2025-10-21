'''
User se temperature (in °C) lo aur condition ke hisaab se print karo:

Agar temperature < 0 → “Freezing weather”

Agar 0 to 10 → “Very Cold”

Agar 11 to 20 → “Cold”

Agar 21 to 30 → “Normal”

Agar 31 to 40 → “Hot”

Agar > 40 → “Very Hot”
'''

temp = int(input("Enter temperature: "))

if temp < 0:
    print("Freezing weather")
elif temp <= 10:
    print("Very Cold")
elif temp <= 20:
    print("Cold")
elif temp <= 30:
    print("Normal")
elif temp <= 40:
    print("Hot")
else:
    print("Very Hot")


