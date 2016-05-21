# Create a variable cars and assign a value of 100

cars = 100

# Create a variable space_in_a_cars and assign a value of 4.0

space_in_a_cars = 4

drivers = 30

passengers = 90

cars_not_driven = cars - drivers

cars_driven = drivers

car_pool_capacity = cars_driven * space_in_a_cars

average_passengers_per_car = passengers/cars_driven

print "There are",cars,"cars avaliable."
print "There are only",drivers,"drivers avaliable."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport", car_pool_capacity,"people taday"
print "We have", passengers, " to carpool today."

print "We need to put about", average_passengers_per_car,"in each car."

