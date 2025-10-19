# This program simulates a health potion that increases the player's health by a random amount between 25 and 50.

import random
health = 50
difficulty = random.randint(1,3)
portion_health = random.randint(25,50)//difficulty
health = health + portion_health
print(health)
