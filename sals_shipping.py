# https://www.codecademy.com/courses/learn-python-3/projects/python-sals-shipping
weight = 41.5

# Ground Shipping 🚚

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $" + str(round(cost_ground, 2)))
# trying to have it as 53.60 with the 0 as showing as a money value..

# Ground Shipping Premimum 🚚💨

cost_ground_premium = 125.00

print("Ground Shipping Premium $" + str(cost_ground_premium))

# Drone Shipping 🛸

if weight <= 2:
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25


print("Drone Shipping $" + str(round(cost_drone, 2)))


# CODECADEMY QUESTION 8
# 4.8 Ibs Ground Shipping is the cheapest at $34.40
# 41.5 Ibs Premium Shipping is the cheapest at $125.00